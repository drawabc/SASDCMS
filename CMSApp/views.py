from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from CMSApp.models import Report
from api.latitudelongitude import get_latlng
from django.urls import reverse
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from authentication import urls
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    report_list = Report.objects.all().filter().order_by("time")
    try:
        postal = request.GET["postal"]
        center = get_latlng(postal)
    except:
        center = -1
    center = json.dumps(center)
    report_list = Report.objects.all()
    haze = get_data()
    markers = []
    for report in report_list:
        markers.append({"name" : report.name, "latlng" : get_latlng(report.postal_code)})
    markers = json.dumps(markers)

    return render(request,"CMSApp/home.html", {'report_list' : report_list, 'center' : center, 'markers' : markers, 'haze': haze})


@login_required
def input(request):
    if request.method == "GET":
        return render(request, "CMSApp/input.html")
    if request.method == "POST":
        try:
            name = request.POST["name"]
            mobile = request.POST["mobile"]
            location = request.POST["location"]
            type = request.POST["type"]
            postal = request.POST["postal"]
            desc = request.POST["description"]
            unit = request.POST["unit"]
            new_report = Report(name=name, mobile=mobile, location=location, type=type, postal_code=postal, description=desc, unit_number=unit)
            new_report.save()
        except:
            return render(request, "CMSApp/input.html", {'error' : 'Error! Please Input Again'})

        return HttpResponseRedirect(reverse('CMSApp:home'))

def detail(request, report_pk):
    report = get_object_or_404(Report, pk=report_pk)
    return render(request, "CMSApp/detail.html", {"report":report})


from api.Facade_API import FacadeAPI
def get_data():
    f = FacadeAPI()
    haze = f.getHaze()
    #dengue = f.getDengue()
    haze_template = {}
    for key, value in haze["location"].items():
        haze_template[key] = {}
        haze_template[key]["location"] = value
    for key, value in haze["psi"].items():
        haze_template[key]["psi"] = value
    for key, value in haze["pm25"].items():
        haze_template[key]["pm25"] = value
    return haze_template

# social media
# sending email
