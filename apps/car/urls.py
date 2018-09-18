from django.contrib import admin
from django.urls import path
from apps.car import views

urlpatterns = [
    path('car/', views.Car),
    #path('admin/', admin.site.urls),
]