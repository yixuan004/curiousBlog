from django.http import HttpResponse
import os

def index(request):

    return HttpResponse("Hello！This is curious main page!!!!")
