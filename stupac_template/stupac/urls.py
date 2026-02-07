from django.urls import path

from stupac import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('admin_home/', views.admin_home, name = 'admin_home'),
    path('enrol_user/', views.enrol_user, name='enrol_user'),
    path('pac_home/', views.pac_home, name='pac_home'),
    path('student_home/', views.student_home, name='student_home'),
    path('view_users_and_asign_pac/', views.view_users_and_asign_pac, name='view_users_and_asign_pac'),
]