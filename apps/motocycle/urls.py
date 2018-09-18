from django.contrib import admin
from django.urls import path
from apps.motocycle import views

urlpatterns = [
    path('motocycle/', views.Motocycle),
    #path('admin/', admin.site.urls),
]