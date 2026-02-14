from django.db import models
from django.db.models import CASCADE


# Create your models here.

#This page will be used to convert the database values into models.
class Admin(models.Model):
    admin_id = models.AutoField(blank=True, primary_key=True)
    first_name = models.TextField(blank=True, null=True,max_length=32)
    last_name = models.TextField(blank=True, null=True,max_length=32)
    email = models.TextField(blank=True, null=True,max_length=64)

    class Meta:
        managed = False
        db_table = 'admin'

class Pac(models.Model):
    pac_id = models.AutoField(blank=True,primary_key=True)
    first_name = models.TextField(blank=True, null=True,max_length=32)
    last_name = models.TextField(blank=True, null=True,max_length=32)
    dob = models.DateField
    gender = models.TextField(blank=True, null=True,max_length=16)
    email = models.TextField(blank=True, null=True,max_length=64)
    department = models.TextField(blank=True, null=True,max_length=64)
    last_edited_when = models.DateTimeField
    last_edited_by = models.ForeignKey("Admin", db_column='last_edited_by', on_delete=CASCADE)
    class Meta:
        managed = False
        db_table = 'pac'

class Student(models.Model):
    student_id = models.AutoField(blank=True,primary_key=True)
    first_name = models.CharField(blank=True, null=True,max_length=32)
    last_name = models.CharField(blank=True, null=True,max_length=32)
    dob = models.DateField
    gender = models.CharField(blank=True, null=True,max_length=16)
    email = models.CharField(blank=True, null=True,max_length=64)
    course = models.CharField(blank=True, null=True,max_length=64)
    assigned_pac = models.ForeignKey("Pac", db_column='assigned_pac', on_delete=CASCADE)
    last_edited_when = models.DateTimeField
    last_edited_by = models.ForeignKey("Admin", db_column='last_edited_by', on_delete=CASCADE)

    class Meta:
        managed = False
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