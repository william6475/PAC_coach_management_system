from django.contrib.auth import authenticate, login

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

#Test user authentication
#sample_user = Pac.objects.create_user(username='Terry Brown ee', password='extremely_secure_password')
#authenticate_user(getattr(sample_user, 'username'), 'extremely_secure_password')
#print(getattr(sample_user, 'username'), 'extremely_secure_password')