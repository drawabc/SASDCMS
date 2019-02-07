from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from CMSApp.models import Report
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    report_list = Report.objects.all().filter().order_by("time")
    try:
        postal = request.GET["postal"]
    except:
        if len(report_list)==0:
            postal = 639218
        else:
            postal = report_list[len(report_list)-1].postal_code
    report_list = Report.objects.all()
    return render(request,"CMSApp/home.html", {'report_list' : report_list, 'postal' : postal})

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



#call center login done
#input form done
# TODO: admin create callcenter
# TODO: home or user dashboard
# TODO: admin dashboard
# TODO: command and control

#social media
#sending email