from pdb import post_mortem
from django.http import HttpResponse
from django.template import loader
import csv
from django.shortcuts import render, redirect
from .forms import view_Form, NewUserForm
from .forms import read_Form
from .models import file_load
from django.views.generic import ListView
import pandas as pd
from pathlib import Path
import re
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    return render(
        request,
        "home.html",
    )


def readme(request):
    return render(
        request,
        "readme.md",
    )


LOG_FILE_TYPES = ["txt", "log"]


@login_required(login_url="/registration/login")
def create_file(request):
    form = view_Form()
    if request.method == "POST":
        form = view_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.upload_file = request.FILES["upload_file"]
            file_type = user_pr.upload_file.url.split(".")[-1]
            file_type = file_type.lower()
            if file_type not in LOG_FILE_TYPES:
                return render(request, "error.html")
            user_pr.save()
            return render(request, "details.html", {"user_pr": user_pr})

    context = {
        "form": form,
    }
    return render(request, "upload.html", context)


@login_required(login_url="/registration/login")
def read_file(request):

    readit = open(
        "media/1603 example.txt",
        "r",
    )
    results = readit.readlines()

    list_lines = []
    idx = 0
    for line in results:
        if "1921" in line:
            list_lines.insert(idx, line)
            idx += 1
            print(line)
            break
        elif "1603" in line:
            list_lines.insert(idx, line)
            idx += 1
            print(line)
            break
        elif "Windows Installer removed" in line:
            list_lines.insert(idx, line)
            idx += 1
            print(line)
            continue
        # else:
        #   print("no results found")
        #  break

    readit.close

    context = {
        "results": list_lines,
    }

    return render(request, "read_file.html", context)


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/upload")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request,
        template_name="registration/register.html",
        context={"register_form": form},
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/upload")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="registration/login.html",
        context={"login_form": form},
    )
