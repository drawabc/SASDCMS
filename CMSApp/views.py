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
import urllib.request as ur
import json
import pprint
from .forms import CivilianForm

# Create your views here.

def home(request):
    report_list = Report.objects.all().filter().order_by("time")
    try:
        postal = request.GET["postal"]
        center = get_latlng(postal)
    except:
        center = -1
    center = json.dumps(center)
    markers = []
    haze = get_haze_data()
    dengue = get_dengue_data()["data"]
    cds = get_cd_shelter()
    for report in report_list:
        markers.append({"name" : report.name, "latlng" : get_latlng(report.postal_code), "type": report.type})
    markers = json.dumps(markers)

    return render(request,"CMSApp/home.html", {'report_list' : report_list, 'center' : center, 'markers' : markers, 'haze': haze, 'dengue':dengue, 'cds': cds})


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

def get_cd_shelter():
    url = 'https://cd-shelter-data.herokuapp.com/'
    url_parser = ur.urlopen(ur.Request(url))
    info = url_parser.read()
    json_dict = json.loads(info.decode('utf-8'))
    return json_dict

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
    form = CivilianForm()
    if request.method == "POST":
        form = CivilianForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('CMSApp:manage'))
        else:
            return render(request, "CMSApp/add_civ.html", {'form': form})
    else:
        return render(request, "CMSApp/add_civ.html", {'form': form})

@login_required
def del_public(request, civ_pk):
    civ_data = get_object_or_404(CivilianData, pk=civ_pk)
    if request.method == "POST":
        civ_data.delete()
        return HttpResponseRedirect(reverse('CMSApp:manage'))
    else:
        return render(request, "CMSApp/del_civ.html", {'civ' : data})

# reference: https://stackoverflow.com/questions/311188/how-do-i-edit-and-delete-data-in-django
# possible better alternative: CivilianData._do_update
# possible better alternative: civ.update_civ_data()
def update_public(request, civ_pk):
        civ_data = get_object_or_404(CivilianData, pk = civ_pk)
        # following code runs if no exception
        if request.method == "GET":
            form = CivilianForm(civ_data)
            return render(request, "CMSApp/add_civ.html", {'form': form})

        elif request.method == "POST":
            form = CivilianForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('CMSApp:manage'))
            else:
                return render(request, "CMSApp/add_civ.html", {'form': form})
        else:
            return render(request, "CMSApp/add_civ.html", {'form': form})