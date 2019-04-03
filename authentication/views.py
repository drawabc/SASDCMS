from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from authentication.forms import CreateAccountForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .decorator import user_is_staff
# Create your views here.

@user_passes_test(user_is_staff)
def manage_dashboard(request):
    user = User.objects.all()
    return render(request, "registration/manage_dashboard.html", {"users": user})

@user_passes_test(user_is_staff)
def signup(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            return HttpResponseRedirect(reverse('authentication:manage_dashboard'))
    else:
        form = CreateAccountForm()
    return render(request, 'registration/signup.html', {'form': form})

@user_passes_test(user_is_staff)
def delete_account(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('authentication:manage_dashboard'))
    else:
        user = get_object_or_404(User, pk=user_pk)
        return render(request, 'registration/delete.html', {'user' : user})

@user_passes_test(user_is_staff)
def reset_password(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.method == 'POST':
        new_pwd = request.POST["pwd"]
        user.set_password(new_pwd)
        return HttpResponseRedirect(reverse('authentication:manage_dashboard'))
    else:
        user = get_object_or_404(User, pk=user_pk)
        return render(request, 'registration/resetpwd.html', {'user': user})

def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    return render(request, 'registration/profile.html')

def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('authentication:profile', args={user.pk}))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/changepwd.html', {
        'form': form
    })