from django.db import models

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

class Pac(models.Model):
    pac_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    last_edited_when = models.DateTimeField()
    last_edited_by = models.ForeignKey(Admin, on_delete=models.CASCADE)

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    assigned_pac = models.ForeignKey(Pac, on_delete=models.CASCADE)
    last_edited_when = models.DateTimeField()
    last_edited_by = models.ForeignKey(Admin, on_delete=models.CASCADE)

# ts is A-U-T-O-MATIC it's like butter

