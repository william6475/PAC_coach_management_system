
from typing import Any

from django.http import HttpResponse
import requests
from django.template import loader


# Views will be created here. These will connect the database to the HTML, and is where most of the backend code will be.
def temp_here(request):
    temp = "TemporaryVariable"
    template = loader.get_template('index.html')
    context = {'temp': temp}
    return HttpResponse(template.render(context, request))