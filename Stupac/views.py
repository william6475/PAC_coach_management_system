from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from Stupac.models import Admin, Pac, Student
from Stupac.tests import is_admin, is_student, is_pac

from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse

# Temporary views for testing
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_home')
    else:
        form = UserCreationForm()
    return render(request, "register.html",{"form":form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('admin_home')
    else:
        form = AuthenticationForm()
    return render(request, "login_test.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('admin_home')

# End of temporary views

# Views created here
def temp_here(request):
    temp = "TemporaryVariable"
    template = loader.get_template('Login.html')
    context = {'temp': temp}
    return HttpResponse(template.render(context, request))

def login_page(request):
    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))


#@login_required
#@user_passes_test(is_admin)
def admin_home(request):
    template = loader.get_template('admin_home.html')
    context = {}
    return HttpResponse(template.render(context, request))

#@login_required
#@user_passes_test(is_student)
def student_home(request):
    student_id = "1" #This is a placeholder, replace with login system authentication
    student_details = Student.objects.raw("Select * from student where student_id = '" + student_id + "'")
    student_pac = str(student_details[0].assigned_pac_id)
    pac_details = Pac.objects.raw("Select * from pac where pac_id = '" + student_pac + "'")
    template = loader.get_template('student_home.html')
    context = {
        'pac_first_name' : pac_details[0].pac_first_name,
        'pac_last_name' : pac_details[0].pac_last_name,
        'pac_email' : pac_details[0].pac_email,
        'pac_department' : pac_details[0].department
    }
    return HttpResponse(template.render(context, request))

#@login_required
#@user_passes_test(is_pac)
def pac_home(request):
    template = loader.get_template('pac_home.html')
    pac_id = "1" #This is a placeholder, replace with login system authentication
    if (request.GET.get("student_name")):
        student_name = request.GET.get("student_name")
    else:
        student_name = ""
    student_details = Student.objects.raw("Select * from student where student_first_name LIKE '%" + student_name + "%' and assigned_pac = '" + pac_id + "'")
    context = {
        'student_details' : student_details,
    }
    return HttpResponse(template.render(context, request))
  
#@login_required
#@user_passes_test(is_admin)
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
        #return redirect("student_home")

    return render(request, "enrol_user.html")

#@login_required
#@user_passes_test(is_admin)
def view_users_and_assign_pac(request):
    students = Student.objects.all()
    pacs = Pac.objects.all()

    if request.method == "POST":
        student_id = request.POST.get("student_id")
        pac_id = request.POST.get("pac_id")

        student = get_object_or_404(Student, pk=student_id)
        student.assigned_pac_id = pac_id
        student.save()

        #return redirect("student_home")

    return render(request, "view_users_and_assign_pac.html", {
        "students": students,
        "pacs": pacs
    })


def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    #return redirect("student_home")

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
        #return redirect("student_home")

    return render(request, "enrol_user.html", {"student": student})


def model_test_admin(request):
    random_item = Admin.objects.all().order_by('?').first()
    temp = random_item.admin_first_name
    template = loader.get_template('model_test.html')
    context = {'random_item': temp}
    return HttpResponse(template.render(context, request))

def model_test_pac(request):
    random_item = Pac.objects.all().order_by('?').first()
    temp = random_item.pac_first_name
    template = loader.get_template('model_test.html')
    context = {'random_item': temp}
    return HttpResponse(template.render(context, request))

def model_test_student(request):
    random_item = Student.objects.all().order_by('?').first()
    temp = random_item.student_first_name
    template = loader.get_template('model_test.html')
    context = {'random_item': temp}
    return HttpResponse(template.render(context, request))