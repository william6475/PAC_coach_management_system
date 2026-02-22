from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.db import models
from django.db.models import CASCADE


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        # tutorial man uses "_create_user()" and "create_user()" and they're two different functions so watch out
        if not email:
            raise ValueError('no valid email provided')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class Generic_User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    first_name = models.CharField(blank=True, default='', max_length=32)
    last_name = models.CharField(blank=True, default='', max_length=32)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_last_name(self):
        return self.last_name


#Admin class
class Admin(Generic_User):
    objects = CustomUserManager()
    
    admin_id = models.AutoField(blank=True, primary_key=True)

    class Meta:
        db_table = 'admin'


# PAC class
class Pac(Generic_User):
    objects = CustomUserManager()

    pac_id = models.AutoField(blank=True, primary_key=True)
    dob = models.DateField
    gender = models.TextField(blank=True, null=True,max_length=16)
    department = models.TextField(blank=True, null=True,max_length=64)

    class Meta:
        db_table = 'pac'

#Student class
class Student(Generic_User):
    objects = CustomUserManager()

    student_id = models.AutoField(blank=True,primary_key=True)
    dob = models.DateField
    gender = models.CharField(blank=True, null=True,max_length=16)
    course = models.CharField(blank=True, null=True,max_length=64)
    assigned_pac = models.ForeignKey("Pac", db_column='assigned_pac', on_delete=CASCADE)

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