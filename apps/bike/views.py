from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Bike(request):
    return render(request,"bike.html")
