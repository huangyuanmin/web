from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Motocycle(request):
    return render(request,"motocycle.html")
