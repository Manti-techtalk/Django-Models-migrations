from django.shortcuts import render
from django.http import HttpRequest

def homePage(request):
    return render(request,'home.html')