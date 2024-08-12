from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib.auth.models import Group
from .models import CustomUser
# from dental.models import BlogPost
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
import os, uuid, json
from uuid import uuid4
from datetime import datetime
from django.utils import timezone
from django.core.mail import send_mail  # later to send mail - send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView
from .forms import NewUForm

# Create your views here.
def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, _("You are now logged in as {}.").format(username))
                return redirect("dashboard")
            else:
                messages.error(request, _("Invalid username or password."))
        else:
            messages.error(request, _("Invalid username or password."))
    form = AuthenticationForm()
    return render(request, "login.html", context={"form":form})

def logout_page(request):
    logout(request)
    messages.info(request, _("You have successfully logged out."))
    return redirect('index')

def register_page(request):
    if request.method == "POST":
        form = NewUForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, _("Registration successful."))
            return redirect("login")
        messages.error(request, _("Unsuccessful registration. Invalid information."))
    form = NewUForm()
    return render (request, "register.html", context={"form":form})
    
@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = PasswordChangeForm(user)
    return render(request, 'password_change_form.html', {'form': form})  



# acquisition of profile photo
# def user_profile(request, iid):
#     post = _____.objects.filter(id=iid)
#     return render(request, "user_profile.html", {'post':post})