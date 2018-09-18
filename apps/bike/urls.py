from django.contrib import admin
from django.urls import path
from apps.bike import views

urlpatterns = [
    path('bike/', views.Bike),
    #path('admin/', admin.site.urls),
]