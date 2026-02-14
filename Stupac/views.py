from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from Stupac.models import Admin, Pac, Student


# from models import name_of_class
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
    return render(request, "view_users_and_assign_pac.html")

def model_test_admin(request):
    random_item = Admin.objects.all().order_by('?').first()
    temp = random_item.first_name
    template = loader.get_template('model_test.html')
    context = {'random_item': temp}
    return HttpResponse(template.render(context, request))

def model_test_pac(request):
    random_item = Pac.objects.all().order_by('?').first()
    temp = random_item.first_name
    template = loader.get_template('model_test.html')
    context = {'random_item': temp}
    return HttpResponse(template.render(context, request))

def model_test_student(request):
    random_item = Student.objects.all().order_by('?').first()
    temp = random_item.first_name
    template = loader.get_template('model_test.html')
    context = {'random_item': temp}
    return HttpResponse(template.render(context, request))