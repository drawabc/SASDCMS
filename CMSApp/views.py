from django.shortcuts import render
from CMSApp.models import Report
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request,"CMSApp/home.html")

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
            new_report = Report(name=name, mobile=mobile, location=location, type=type)
            new_report.save()
        except:
            return render(request, "CMSApp/input.html", {'error' : 'Error! Please Input Again'})

        return render(request, "CMSApp/input.html", {'error' : 'none'})
#call center login
#admin call center create
#call center dashboard
#call center input form
#home = user dashboard
#admin dashboard
#sending email later