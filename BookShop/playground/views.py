from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action

def home(request):
    return HttpResponse("Hello, Django")