from django.contrib import admin
from django.urls import path
from apps.login import views

urlpatterns = [
    path('login/', views.login),
    path('admin/', admin.site.urls),
]