from django.contrib import admin
from .models import Student,Pac, Admin
# Register your models here.
from .models import Generic_User

admin.site.register(Generic_User)
admin.site.register(Student)
admin.site.register(Pac)
admin.site.register(Admin)