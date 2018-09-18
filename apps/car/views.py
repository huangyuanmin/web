from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Car(request):
    return render(request,"car.html")
