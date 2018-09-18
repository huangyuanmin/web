from django.contrib import admin
from apps.login.models import register_form
from apps.login.models import login_fform


# Register your models here.


class register_formAdmin(admin.ModelAdmin):
    list_register = ['r_user_name', 'r_password']


class login_fformAdmin(admin.ModelAdmin):
    list_register = ['user_name', 'password']



admin.site.register(register_form, register_formAdmin)
admin.site.register(login_fform, login_fformAdmin)