from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def welcome(request):
    return HttpResponse("welcome to my page")


def hello(request, name):
    return render(request, 'hello.html', {'name': name})


def numbers(request, number):
    return HttpResponse(number)
