from django.urls import path
from Stupac import views
from . import views

urlpatterns = [
    path("students/", views.student_home, name="student_home"),
    path("students/create/", views.enrol_User, name="enrol_user"),
    path("students/edit/<int:student_id>/", views.edit_student, name="edit_student"),
    path("students/delete/<int:student_id>/", views.delete_student, name="delete_student"),
    path("students/assign/", views.view_users_and_assign_pac, name="assign_pac"),
]1
urlpatterns = [
    path('', views.login, name = 'login'),
    path('admin_home/', views.admin_home, name = 'admin_home'),
    path('enrol_user/', views.enrol_user, name='enrol_user'),
    path('pac_home/', views.pac_home, name='pac_home'),
    path('student_home/', views.student_home, name='student_home'),
    path('view_users_and_asign_pac/', views.view_users_and_asign_pac, name='view_users_and_asign_pac'),

    path('models_test/admin',views.model_test_admin, name = 'model_test_admin'),
    path('models_test/pac',views.model_test_pac, name = 'model_test_pac'),
    path('models_test/student',views.model_test_student, name = 'model_test_student'),
]