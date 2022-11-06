from pdb import post_mortem
from django.shortcuts import render

from django.shortcuts import render
from .forms import view_Form
from .models import file_load
from django.views.generic import ListView


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
