
from typing import Any

from django.http import HttpResponse
import requests
from django.template import loader
from django.shortcuts import render


# Views will be created here. These will connect the database to the HTML, and is where most of the backend code will be.
def temp_here(request):
    temp = "TemporaryVariable"
    template = loader.get_template('Login.html')
    context = {'temp': temp}
    return HttpResponse(template.render(context, request))

def login(request):
    return render(request, "login.html")

def admin_home(request):
    return render(request, "admin_home.html")

def student_home(request):
    return render(request, "student_home.html")

def pac_home(request):
    return render(request, "pac_home.html")

def enrol_user(request):
    return render(request, "enrol_user.html")

def view_users_and_asign_pac(request):
    return render(request, "view_users_and_asign_pac.html")