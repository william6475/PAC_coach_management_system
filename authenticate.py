from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from Stupac.models import Pac, Student, Admin

#Authenticates user login requests
def authenticate_user(request, username, password):
    user_exists = authenticate(username=username, password=password)
    if user_exists != None:
        login(request, user_exists)

        # Redirect the logged in user to the corresponding home page
        if user_exists.__class__.__name__ == "Student":
            return (redirect("/student_home"))
        elif user_exists.__class__.__name__ == "Admin":
            return (redirect("/admin_home"))
        elif user_exists.__class__.__name__ == "Pac":
            return (redirect("/pac_home"))
        else:
            return ("User type error. An invalid user type was found with those loggin details")

    if user_exists == None:

        return("user_not_found")
    else:

        return("authentication_error")

#Logs out user
def logout_user(request):
    logout(request)