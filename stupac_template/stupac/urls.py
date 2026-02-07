from django.urls import path

from stupac import views

urlpatterns = [
    path("stupac/",views.temp_here, name = "temp_here")
]