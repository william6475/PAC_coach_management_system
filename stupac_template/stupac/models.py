from django.db import models

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'admin'

class Pac(models.Model):
    pac_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateField()
    gender = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    last_edited_when = models.DateTimeField()
    last_edited_by = models.ForeignKey(Admin, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'pac'

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateField()
    gender = models.CharField(max_length=16)
    email = models.CharField(max_length=64)
    course = models.CharField(max_length=64)
    assigned_pac = models.ForeignKey(Pac, on_delete=models.CASCADE)
    last_edited_when = models.DateTimeField()
    last_edited_by = models.ForeignKey(Admin, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'student'

