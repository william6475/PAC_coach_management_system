from django.contrib.auth import authenticate, login, logout

from Stupac.models import Pac, Student, Admin

#Authenticates user login requests
def authenticate_user(request, username, password):
    user_exists = authenticate(username=username, password=password)
    if user_exists != None:
        login(request, user_exists)
        return("login successful")
    if user_exists == None:

        return("user_not_found")
    else:

        return("authentication_error")

#Logs out user
def logout_user(request):
    logout(request)