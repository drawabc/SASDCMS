from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from CMSApp.models import Report, CivilianData
from apis.latitudelongitude import get_latlng
from django.urls import reverse
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from authentication import urls
from django.core.mail import send_mail
from django.conf import settings
from .forms import AddCivilianForm, EditCivilianForm

# Create your views here.

def home(request):
    report_list = Report.objects.all().filter().order_by("time")
    try:
        postal = request.GET["postal"]
        center = get_latlng(postal)
    except:
        center = -1
    center = json.dumps(center)
    haze = get_haze_data()
    markers = []
    dengue = get_dengue_data()
    dengue = json.dumps({})
    #print(len(dengue))
    for report in report_list:
        markers.append({"name" : report.name, "latlng" : get_latlng(report.postal_code), "type": report.type})
    markers = json.dumps(markers)

    return render(request,"CMSApp/home.html", {'report_list' : report_list, 'center' : center, 'markers' : markers, 'haze': haze, 'dengue':dengue})


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

from apis.Facade_API import FacadeAPI
f = FacadeAPI()

@login_required
def archive(request):
    all_reports = Report.objects.all()
    return render(request, "CMSApp/archive.html", {'all_reports': all_reports})

def somethingnew(request):
    return JsonResponse({'foo': 'bar'})

def get_haze_data():
    haze = f.getHaze()
    haze_template = {}
    for key, value in haze["location"].items():
        haze_template[key] = {}
        haze_template[key]["location"] = value
    for key, value in haze["psi"].items():
        haze_template[key]["psi"] = value
    for key, value in haze["pm25"].items():
        haze_template[key]["pm25"] = value
    return haze_template

import urllib.request as ur
import json
import pprint
def get_dengue_data():
    url = 'https://api-scheduler.herokuapp.com/'
    url_parser = ur.urlopen(ur.Request(url))
    info = url_parser.read()
    json_dict = json.loads(info.decode('utf-8'))
    return json_dict

@login_required()
def manage_public(request):
    civ_list = CivilianData.objects.all()
    return render(request, "CMSApp/manage_civ.html", {'civ_list' : civ_list})

#feel free to refactor code below
def add_public(request):
    if request.method == "POST":
        nric = request.POST["nric"]
        name = request.POST["name"]
        mobile = request.POST["mobile"]
        email = request.POST["email"]
        region = request.POST["region"]

        new_civ_data = CivilianData(nric=nric,name=name,mobile=mobile,email=email,region=region)
        try:
            new_civ_data.save()
            return HttpResponseRedirect(reverse('CMSApp:home'))
        except:
            return render(request, "CMSApp/add_civ.html", {'form':AddCivilianForm(), 'error' : 'Error! NRIC is already in use.'})
    else:
        return render(request, "CMSApp/add_civ.html", {'form':AddCivilianForm()})

#not sure if this is correct (or if any of the code i wrote here is correct)
def verify_nric(request):
    if request.method == "POST":
        return get_object_or_404(CivilianData, pk=request.POST["NRIC"])
    else:
        return render(request, "CMSApp/what to display?.html", {'form':EditCivilianForm()}) # TODO: wait for Jun En's magic

def edit_public(request):
    if request.method == "POST":
        # TODO: wait for Jun En's magic
        form = EditCivilianForm(initial={"nric":request.POST["nric"], "name":request.POST["name"],
                "mobile":request.POST["mobile"],"email":request.POST["email"],"region":request.POST["region"]})
        return render(request, "CMSApp/what to display?.html", {'form':form}) 


# https://stackoverflow.com/questions/311188/how-do-i-edit-and-delete-data-in-django
# this function makes sense if the caller is an "Update" button
def update_civ_data(request, nric):
    # possible better alternative: CivilianData._do_update
    # possible better alternative: civ.update_civ_data()

    try:
        civ = CivilianData.objects.get(pk = nric)
        try:
            civ.nric = CivilianData.objects.get(pk = request.POST.get("nric"))
            return HttpResponse('nric exists already')
        except CivilianData.D:
            civ.nric = request.POST.get("nric")

        civ.name = request.POST.get("name")
        civ.mobile = request.POST.get("mobile")
        civ.email = request.POST.get("email")
        civ.region = request.POST.get("region")

        civ.save()
        return HttpResponse('updated civilian data') # what do i return?
    except:
        return HttpResponse('civilian does not exist') # what do i return?

# https://stackoverflow.com/questions/311188/how-do-i-edit-and-delete-data-in-django
# this function makes sense if the caller is an "Delete" button
def delete_civ_data(request, nric):
    try:
        civ = CivilianData.objects.get(pk = nric)
        civ.delete()
        return HttpResponse('deleted civilian data') # what do i return?
    except:
        return HttpResponse('civilian does not exist') # what do i return
            