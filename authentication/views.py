from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from authentication.forms import CreateAccountForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

@login_required
def manage_dashboard(request):
    user = User.objects.all()
    return render(request, "registration/manage_dashboard.html", {"user": user})

def signup(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return HttpResponseRedirect(reverse('manage_dashboard'))
    else:
        form = CreateAccountForm()
    return render(request, 'registration/signup.html', {'form': form})