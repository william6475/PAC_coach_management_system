
from Stupac.models import Admin, Student, Pac


# Create your tests here.

def is_admin(user):
    if isinstance(user, Admin):
        return True
    else:
        return False
def is_student(user):
    if isinstance(user, Student):
        return True
    else:
        return False
def is_pac(user):
    if isinstance(user, Pac):
        return True
    else:
        return False