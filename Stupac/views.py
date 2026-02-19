# need to commit.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from Stupac.models import Admin, Pac, Student


# from models import name_of_class

from .models import Student, Pac
from django.shortcuts import render, redirect, get_object_or_404


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

#def student_home(request):
    return render(request, "student_home.html")

def student_home(request):
    students = Student.objects.all()
    return render(request, "student_home.html", {"students": students})

def pac_home(request):
    return render(request, "pac_home.html")

#def enrol_user(request):
    return render(request, "enrol_user.html")
def enrol_user(request):
    if request.method == "POST":
        Student.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            gender=request.POST.get("gender"),
            dob=request.POST.get("dob"),
            email=request.POST.get("email"),
            course=request.POST.get("course"),
        )
        return redirect("student_home")

    return render(request, "enrol_user.html")

#def view_users_and_asign_pac(request):
    return render(request, "view_users_and_assign_pac.html")
def view_users_and_asign_pac(request):
    students = Student.objects.all()
    pacs = Pac.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student_id")
        pac_id = request.POST.get("pac_id")

        student = get_object_or_404(Student, pk=student_id)
        student.assigned_pac_id = pac_id
        student.save()

        return redirect("student_home")

    return render(request, "view_users_and_assign_pac.html", {
        "students": students,
        "pacs": pacs
    })

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect("student_home")

def edit_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == "POST":
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.gender = request.POST.get("gender")
        student.dob = request.POST.get("dob")
        student.email = request.POST.get("email")
        student.course = request.POST.get("course")
        student.save()
        return redirect("student_home")

    return render(request, "enrol_user.html", {"student": student})


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