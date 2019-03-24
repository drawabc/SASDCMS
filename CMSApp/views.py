from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from CMSApp.models import Report
from django.urls import reverse
from django.core import serializers
import json
from CMSApp.api.latitudelongitude import get_latlng
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
    markers = []
    for report in report_list:
        markers.append({"name" : report.name, "latlng" : get_latlng(report.postal_code)})
    markers = json.dumps(markers)

    return render(request,"CMSApp/home.html", {'report_list' : report_list, 'center' : center, 'markers' : markers})


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
            new_report = Report(name=name, mobile=mobile, location=location, type=type, postal_code=postal)
            new_report.save()
        except:
            return render(request, "CMSApp/input.html", {'error' : 'Error! Please Input Again'})

        return HttpResponseRedirect(reverse(home))

def detail(request, report_pk):
    report = get_object_or_404(Report, pk=report_pk)
    return render(request, "CMSApp/detail.html", {"report":report})

from api.Email.email import EmailSend

def email():
    e = EmailSend()
    server = e.startServer()
    print(e.send_email(server, ['echristo001@e.ntu.edu.sg'], 'GG MATE', 'CMS APP'))
    e.quitServer(server)

# social media
# sending email