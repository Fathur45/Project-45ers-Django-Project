from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def homepage(response):
    return render(response, 'Homepage 3a7c0.html', {"name": "test"})


def collab(response):
    return render(response, 'Homepage 3a7c0/Collaborat 456bd.html')


def company(response):
    return render(response, 'Homepage 3a7c0/Company 84863.html')


def profile(response):
    return render(response, 'Homepage 3a7c0/Profile 43b49.html')


def service(response):
    return render(response, 'Homepage 3a7c0/Service 047aa.html')


def v1(response):
    return render(response, 'home.html')
