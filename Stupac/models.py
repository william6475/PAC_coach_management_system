from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import CASCADE


# Create your models here.

#Generic user class used for user authentication
#Usefull fields inherited from AbstractUser: Username / Password / email / first_name / last_name
class Generic_user(AbstractUser):
    generic_user_id = models.AutoField(blank=True, primary_key=True)

#Admin class
class Admin(Generic_user):
    objects = UserManager()
    
    admin_id = models.AutoField(blank=True, primary_key=True)

    class Meta:
        db_table = 'admin'

#PAC class
class Pac(Generic_user):
    objects = UserManager()

    pac_id = models.AutoField(blank=True,primary_key=True)
    dob = models.DateField
    gender = models.TextField(blank=True, null=True,max_length=16)
    department = models.TextField(blank=True, null=True,max_length=64)
    last_edited_when = models.DateTimeField
    last_edited_by = models.ForeignKey("Admin", db_column='last_edited_by', on_delete=CASCADE, null=True, blank=True)
    class Meta:
        db_table = 'pac'

#Student class
class Student(Generic_user):
    objects = UserManager()

    student_id = models.AutoField(blank=True,primary_key=True)
    dob = models.DateField
    gender = models.CharField(blank=True, null=True,max_length=16)
    course = models.CharField(blank=True, null=True,max_length=64)
    assigned_pac = models.ForeignKey("Pac", db_column='assigned_pac', on_delete=CASCADE)
    last_edited_when = models.DateTimeField
    last_edited_by = models.ForeignKey("Admin", db_column='last_edited_by', on_delete=CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'student'

"""
OLD code


class Admin(models.Model):
    admin_id = models.TextField(blank=True, primary_key=True)  # This field type is a guess.
    first_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'admin'

class Pac(models.Model):
    pac_id = models.TextField(blank=True, null=True)  # This field type is a guess.
    first_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    dob = models.TextField(blank=True, null=True)  # This field type is a guess.
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    department = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_edited_when = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_edited_by = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pac'

"""