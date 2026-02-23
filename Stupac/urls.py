
from django.urls import path
from Stupac import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.login_view, name='login_page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('enrol_user/', views.enrol_user, name='enrol_user'),
    path('pac_home/',views.pac_home, name='pac_home'),
    #path('pac_home/?student_name=', views.pac_home, name='pac_home'),
    path('student_home/', views.student_home, name='student_home'),
    path('view_users_and_assign_pac/', views.view_users_and_assign_pac, name='view_users_and_assign_pac'),
    path('students/', views.student_home, name='student_list'),
    path('students/create/', views.enrol_user, name='student_create'),
    path('students/assign/', views.view_users_and_assign_pac, name='assign_pac'),
    path('models_test/admin', views.model_test_admin, name='model_test_admin'),
    path('models_test/pac', views.model_test_pac, name='model_test_pac'),
    path('models_test/student', views.model_test_student, name='model_test_student'),
    path('register/',views.register_home, name = 'register_home'),
    path('register/student',views.register_student, name = 'register_student'),
    path('register/pac',views.register_pac, name = 'register_pac'),
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# /* from django.urls import path
# from Stupac import views
#
# urlpatterns = [7
#     path('', views.login, name = 'login'),
#     path('admin_home/', views.admin_home, name = 'admin_home'),
#     path('enrol_user/', views.enrol_user, name='enrol_user'),
#     path('pac_home/', views.pac_home, name='pac_home'),
#     path('student_home/', views.student_home, name='student_home'),
#     path('view_users_and_assign_pac/', views.view_users_and_assign_pac, name='view_users_and_assign_pac'),
#
#     path('models_test/admin',views.model_test_admin, name = 'model_test_admin'),
#     path('models_test/pac',views.model_test_pac, name = 'model_test_pac'),
#     path('models_test/student',views.model_test_student, name = 'model_test_student'),
# ] */
