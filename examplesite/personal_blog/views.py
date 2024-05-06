from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "personal_blog/welcome.html")

def about_me(request):
    return render(request, "personal_blog/about_me.html")   

def cv(request):
    return render(request, "personal_blog/cv.html")

def socials(request):
    return render(request, "personal_blog/socials.html")


