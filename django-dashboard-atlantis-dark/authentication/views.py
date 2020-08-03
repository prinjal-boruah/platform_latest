# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg1 = None
    msg = None
    success = False

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/projects")
            else:    
                msg1 = 'Invalid credentials'    
        else:
            msg1 = 'Error validating the form'
      
        reg_form = SignUpForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data.get("username")
            raw_password = reg_form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            msg = 'User created.'
            success = True
            login(request, user)
            return redirect("create_project")
        else:
            msg = 'Form is not valid'

    else:
        reg_form = SignUpForm()

    return render(request, "accounts/login.html", {"form": form, "msg" : msg, "success" : success, "reg_form": reg_form})

def register_user(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            msg = 'User created.'
            success = True
        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
