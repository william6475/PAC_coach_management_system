from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import Student, Pac

"""
class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pac_first_name = forms.CharField(max_length=32,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    pac_last_name = forms.CharField(max_length=32,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Stupac.models.Student
        fields = ("pac_first_name", "pac_last_name")

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = models.Generic_User
        fields = ( "email", "first_name", "last_name", "password1", "password2")
        
class PacRegistrationForm(UserCreationForm):
    pac_first_name = forms.CharField()
    pac_last_name = forms.CharField()
    gender = forms.CharField()
    department = forms.CharField()
    class Meta:
        model = models.Pac
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
        fields = ( "email", "student_first_name", "student_last_name",  "gender","course","pac_first_name","pac_last_name", "password1", "password2")
"""
