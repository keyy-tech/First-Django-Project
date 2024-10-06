from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action


def hompage(request):
    return render(request, "home.html")
    # return HttpResponse("Hello World! I'm Home")


def about(request):
    return render(request, "about.html")
    # return HttpResponse("About Me")
