from django.shortcuts import render

from django.http import HttpResponse


def form(request):
    return render(request,'myapp/form.html')

def index(request):
    return render(request,'myapp/index.html')

def about(request):
    return render(request,'myapp/about.html')

def registration(request):
    return render(request,'myapp/registration.html')