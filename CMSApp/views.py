import json
import urllib.request as ur

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from CMSApp.models import Report, CivilianData
from apis.latitudelongitude import get_latlng
from apis.sms_django import SMSAPI
from .forms import CivilianForm


# Create your views here.

def home(request):
    report_list = Report.objects.all().filter().order_by("time")[:5:-1]
    try:
        postal = request.GET["postal"]
        center = get_latlng(postal)
    except:
        center = -1
    center = json.dumps(center)
    markers = []
    data = get_server_data()
    haze = get_haze_data(data)
    print(haze)
    dengue = get_dengue_data(data)
    cds = get_cd_shelter(data)
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
            type1 = request.POST["type"]
            postal = request.POST["postal"]
            desc = request.POST["description"]
            unit = request.POST["unit"]
            django_dict = {}
            django_dict["Type"] = str(type1)
            django_dict["mobile"] = str(mobile)
            django_dict["Location"] = str(location)
            django_dict["postal"] = str(postal)
            django_dict["Description"] = str(desc)
            django_dict["name"] = str(name)

            new_report = Report(name=name, mobile=mobile, location=location, type=type1, postal_code=postal, description=desc, unit_number=unit)
            new_report.save()
            #Sending SMS
            sender = "+12052939421"
            receiverAgency = ['+6596579895']
            sms = SMSAPI()
            #Hard coded this for now because sms uses twilio server which is severely limited to a number of phones
            receiver_region = ["+6591746880", "+6586502577", "+6598835026", "+6582965839", "+6591746880"]
            print(sms.sendFormattedSMS(django_dict, sender,receiverAgency))
            print(sms.sendFormattedSMS(django_dict, sender, receiver_region))
        except:
            return render(request, "CMSApp/input.html", {'error' : 'Error! Please Input Again'})

        return HttpResponseRedirect(reverse('CMSApp:home'))

def detail(request, report_pk):
    report = get_object_or_404(Report, pk=report_pk)
    return render(request, "CMSApp/detail.html", {"report":report})


@login_required
def archive(request):
    all_reports = Report.objects.all()
    return render(request, "CMSApp/archive.html", {'all_reports': all_reports})


def get_server_data():
    url = 'https://api-scheduler.herokuapp.com/'
    url_parser = ur.urlopen(ur.Request(url))
    info = url_parser.read()
    json_dict = json.loads(info.decode('utf-8'))
    return json_dict

def get_cd_shelter(dict):
    if dict=={}:
        return {}
    else:
        return dict["data_cdshelter"]

def get_haze_data(dict):
    if dict=={}:
        return {"location":{}, "psi":{}, "pm25":{}}
    else:
        haze = dict["data_haze"]
        haze_template = {}
        for key, value in haze["location"].items():
            haze_template[key] = {}
            haze_template[key]["location"] = value
        for key, value in haze["psi"].items():
            haze_template[key]["psi"] = value
        for key, value in haze["pm25"].items():
            haze_template[key]["pm25"] = value
        return haze_template

def get_dengue_data(dict):
    if dict=={}:
        return {}
    else:
        return dict["data_dengue"]

@login_required
def manage_public(request):
    civ_list = CivilianData.objects.all()
    return render(request, "CMSApp/manage_civ.html", {'civ_list' : civ_list})

@login_required
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
        return render(request, "CMSApp/del_civ.html", {'civ' : civ_data})

# reference: https://stackoverflow.com/questions/311188/how-do-i-edit-and-delete-data-in-django
# possible better alternative: CivilianData._do_update
# possible better alternative: civ.update_civ_data()
@login_required
def update_public(request, civ_pk):
    civ_data = get_object_or_404(CivilianData, pk=civ_pk)
    # following code runs if no exception
    if request.method == "POST":
        form = CivilianForm(request.POST, instance=civ_data)
        print(request.POST["name"])
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('CMSApp:manage'))
        else:
            return render(request, "CMSApp/update_civ.html", {'civ': civ_data})
    else:
        # request.method == "GET"
        form = CivilianForm(instance=civ_data)
        return render(request, "CMSApp/update_civ.html", {'civ': civ_data})