from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
import Stupac.models
import Stupac.tests
from Stupac.models import Admin, Pac, Student, Generic_User
from Stupac.tests import is_admin, is_student, is_pac

from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse


# Temporary views for testing
class UpdateUserForm(UserChangeForm):
    #student_email = forms.CharField(max_length=32,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    pac_first_name = forms.CharField(max_length=32,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    pac_last_name = forms.CharField(max_length=32,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Stupac.models.Student
        fields = ("email","pac_first_name", "pac_last_name")

def is_user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
# End of temporary views


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = Stupac.models.Generic_User
        fields = ( "email", "first_name", "last_name", "password1", "password2")

class PacRegistrationForm(UserCreationForm):
    pac_first_name = forms.CharField()
    pac_last_name = forms.CharField()
    gender = forms.CharField()
    department = forms.CharField()
    class Meta:
        model = Stupac.models.Pac
        fields = ( "email", "pac_first_name", "pac_last_name", "gender","department", "password1", "password2")


class StudentRegistrationForm(UserCreationForm):
    student_first_name = forms.CharField()
    student_last_name = forms.CharField()
    gender = forms.CharField()
    course = forms.CharField()
    pac_first_name = forms.CharField()
    pac_last_name = forms.CharField()
    class Meta:
        model = Stupac.models.Student
        fields = ("email", "student_first_name", "student_last_name",  "gender","course","pac_first_name","pac_last_name", "password1", "password2")


def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_users')
    else:
        form = StudentRegistrationForm()
    return render(request, "register.html",{"form":form, "input_name" : 'Student'})

def register_pac(request):
    if request.method == "POST":
        form = PacRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_users')
    else:
        form = PacRegistrationForm()
    return render(request, "register.html",{"form":form, "input_name" : 'Pac'})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user_email = str(form.get_user())
            login(request, form.get_user())
            try:
                student_user = Student.objects.get(student_email=user_email)
                return redirect('student_home')
            except:
                print("No student with matching credentials")
            try:
                pac_user = Pac.objects.get(pac_email=user_email)
                return redirect('pac_home')
            except:
                print("No pac with matching credentials")
            try:
                admin_user = Admin.objects.get(admin_email=user_email)
                return redirect('admin_home')
            except:
                print("No admin with matching credentials")
            #student_result = Student.objects.raw("select student_id from student where student_email = '"+user_email+"'")
            #pac_result = Pac.objects.raw("select pac_id from pac where pac_email = '" + user_email + "'")
            #admin_result = Admin.objects.raw("select admin_id from admin where admin_email = '" + user_email + "'")
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('admin_home')
    else:
        form = AuthenticationForm()
    return render(request, "login_test.html", {"form": form})

@login_required(login_url="/login/")
def logout_view(request):
    if request.method == "POST":
        logout(request)
        redirect('admin_home')
    return render(request, "login.html")

# Views created here
def temp_here(request):
    temp = "TemporaryVariable"
    template = loader.get_template('Login.html')
    context = {'temp': temp}
    return HttpResponse(template.render(context, request))

def register_home(request):
    template = loader.get_template('register_home.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
#@user_passes_test(is_admin)
def admin_home(request):
    template = loader.get_template('admin_home.html')
    generic_id = str(request.user.id)
    try:
        pact_user = Pac.objects.get(generic_user_ptr_id=generic_id)
        return redirect('login')
    except:
        a = 0
    try:
        student_user = Student.objects.get(generic_user_ptr_id=generic_id)
        return redirect('login')
    except:
        a = 0
    """
    # These lines of code auto-assigns email to admin.
    user = Admin.objects.get(generic_user_ptr_id=generic_id)
    get_email = Generic_User.objects.raw("select id, email from Stupac_generic_user where id = '" + generic_id + "'")
    admin_email = str(get_email[0].email)
    user.admin_email = admin_email
    user.save(update_fields=['admin_email'])
    """
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url="/login/")
#@user_passes_test(is_student)
def student_home(request):
    #student_id = "1" #This is a placeholder, replace with login system authentication
    generic_id = str(request.user.id)
    try:
        student_user = Student.objects.get(generic_user_ptr_id=generic_id)
    except:
        return redirect('login')
    #setStudentEmail(generic_id)
    get_email = Generic_User.objects.raw("select id, email from Stupac_generic_user where id = '" + generic_id + "'")
    student_email = str(get_email[0].email)
    fetch_student_id = Student.objects.raw("Select student_id from student where generic_user_ptr_id = '"+generic_id+"'")
    student_id = str(fetch_student_id[0].student_id)

    user = Student.objects.get(student_id=student_id)
    user.student_email = student_email
    user.save(update_fields=['student_email'])

    student_details = Student.objects.raw("Select * from student where student_id = '" + student_id + "'")
    student_pac_fname = str(student_details[0].pac_first_name)
    student_pac_lname = str(student_details[0].pac_last_name)
    pac_details = Pac.objects.raw("Select * from pac where pac_first_name = '" + student_pac_fname + "' and pac_last_name = '"+student_pac_lname+"'")
    template = loader.get_template('student_home.html')
    context = {
        'pac_first_name' : pac_details[0].pac_first_name,
        'pac_last_name' : pac_details[0].pac_last_name,
        'pac_email' : pac_details[0].pac_email,
        'pac_department' : pac_details[0].department
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
#@user_passes_test(is_pac)
def pac_home(request):
    template = loader.get_template('pac_home.html')
    generic_id = str(request.user.id)
    try:
        pact_user = Pac.objects.get(generic_user_ptr_id=generic_id)
    except:
        return redirect('login')
    get_email = Generic_User.objects.raw("select id, email from Stupac_generic_user where id = '" + generic_id + "'")
    pac_email = str(get_email[0].email)
    fetch_pac_id = Pac.objects.raw(
        "Select pac_id from pac where generic_user_ptr_id = '" + generic_id + "'")
    pac_id = str(fetch_pac_id[0].pac_id)

    user = Pac.objects.get(pac_id=pac_id)
    user.pac_email = pac_email
    user.save(update_fields=['pac_email'])


    fetch_pac_name = Pac.objects.raw(
        "Select pac_first_name, pac_id from pac where generic_user_ptr_id = '" + generic_id + "'")
    if fetch_pac_name[0].pac_first_name is not None:
        pac_name= str(fetch_pac_name[0].pac_first_name)
    #pac_id = "2" #This is a placeholder, replace with login system authentication
    #pac_details = Pac.objects.raw("Select * from pac where pac_id = '" + pac_id+"'")
    pac_details = Pac.objects.raw("Select * from pac where pac_first_name = '"+pac_name+"'") #This is a placeholder, replace with login system authentication
    if pac_details[0].pac_first_name is not None:
        pac_fname = str(pac_details[0].pac_first_name)
    if pac_details[0].pac_last_name is not None:
        pac_lname = str(pac_details[0].pac_last_name)
    if request.GET.get("student_name"):
        student_name = request.GET.get("student_name")
    else:
        student_name = ""
    #The line below may flag an error, but is correct.
    student_details = Student.objects.raw("Select * from student where student_first_name LIKE '%" + student_name + "%' and pac_first_name = '" + pac_fname + "' and pac_last_name = '"+pac_lname+"'")
    context = {
        'student_details' : student_details,
    }
    return HttpResponse(template.render(context, request))

def student_details(request):
    template = loader.get_template('student_details.html')
    student_email = request.GET.get("student_email") #alternative option
    student = Student.objects.get(student_email=student_email)
    context = {
        'student_first_name' : student.student_first_name,
        'student_last_name' : student.student_last_name,
        'student_email' : student.student_email,
        'gender' : student.gender,
        'course' : student.course,
        'pac_first_name' : student.pac_first_name,
        'pac_last_name' : student.pac_last_name,
    }
    return HttpResponse(template.render(context, request))

def user_details(request):
    template = loader.get_template('user_details.html')
    user_email = str(request.GET.get("user_email")) #alternative option
    get_id = Generic_User.objects.raw("select id, email from Stupac_generic_user where email = '" + user_email + "'")
    try:
        student_user = Student.objects.get(generic_user_ptr_id=get_id)
        student_user.student_email = user_email
        student_user.save(update_fields=['student_email'])
    except:
        print("No Student with matching credentials")
    try:
        student_user = Pac.objects.get(generic_user_ptr_id=get_id)
        student_user.pac_email = user_email
        student_user.save(update_fields=['pac_email'])
    except:
        print("No Pac with matching credentials")
    try:
        student_user = Admin.objects.get(generic_user_ptr_id=get_id)
        student_user.admin_email = user_email
        student_user.save(update_fields=['admin_email'])
    except:
        print("No Admin with matching credentials")


    """
    generic_id = str(request.user.id)
    try:
        student_user = Student.objects.get(generic_user_ptr_id=generic_id)
    except:
        return redirect('login')
    #setStudentEmail(generic_id)
    get_email = Generic_User.objects.raw("select id, email from Stupac_generic_user where id = '" + generic_id + "'")
    student_email = str(get_email[0].email)
    fetch_student_id = Student.objects.raw("Select student_id from student where generic_user_ptr_id = '"+generic_id+"'")
    student_id = str(fetch_student_id[0].student_id)

    user = Student.objects.get(student_id=student_id)
    user.student_email = student_email
    user.save(update_fields=['student_email'])
    """


    first_name = ""
    last_name = ""
    email = ""
    gender = ""
    course = ""
    try:
        #Pac.objects.get(pac_email=user_email) == user_email
        user = Pac.objects.get(pac_email=user_email)
        first_name = user.pac_first_name
        last_name = user.pac_last_name
        email = user.pac_email
        gender = user.gender
        course = user.department
    except:
        print("No Pac with matching credentials")
    try:
        Student.objects.get(student_email=user_email)
        user = Student.objects.get(student_email=user_email)
        first_name = user.student_first_name
        last_name = user.student_last_name
        email = user.student_email
        gender = user.gender
        course = user.course
    except:
        print ("No Student with matching credentials")
    context = {
        'student_first_name' : first_name,
        'student_last_name' : last_name,
        'student_email' : email,
        'gender' : gender,
        'course' : course,
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

    return render(request, "enrol_user.html")


def view_users(request):
    template = loader.get_template('view_users.html')
    if request.GET.get("user_name"):
        user_name = request.GET.get("user_name")
    else:
        user_name=""
    user_emails = Generic_User.objects.raw("select id, email from main.Stupac_generic_user where email LIKE '%" + user_name + "%'")

    context = {"user_emails" : user_emails}
    return HttpResponse(template.render(context, request))

@login_required(login_url="/login/")
def assign_pac(request):

    #This method does not work
    if request.method == 'POST':
        student_email = str(request.POST.get("student_email"))
        pac_first_name = str(request.POST.get("pac_first_name"))
        pac_last_name = str(request.POST.get("pac_last_name"))
        student = Student.objects.get(student_email=student_email)
        student.pac_first_name = pac_first_name
        student.pac_last_name = pac_last_name
        student.save(update_fields=['pac_first_name','pac_last_name'])
    return render(request, 'assign_pac.html', {})


#@login_required
#@user_passes_test(is_admin)
def view_users_and_assign_pac(request):
    if request.GET.get("user_name"):
        user_name = request.GET.get("user_name")
    else:
        user_name=""
    # A problem with this query causes the results list to break when user_name is not empty
    user_emails = Generic_User.objects.raw("select id, email from main.Stupac_generic_user where email LIKE '%" + user_name + "%'")

    if request.method == "POST":
        student_email = str(request.POST.get("student_email"))
        pac_first_name = str(request.POST.get("pac_first_name"))
        pac_last_name = str(request.POST.get("pac_last_name"))
        pac_assignment = Student.objects.raw("update main.student set pac_first_name = '" + pac_first_name + "', pac_last_name = '" + pac_last_name + "' where student_email = '" + student_email + "'")
        assignment_status = True
    else:
        assignment_status = False
    return render(request, "view_users_and_assign_pac.html", {
        "user_emails" : user_emails,
        "assignment_status" : assignment_status,
    })