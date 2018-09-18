from django.db import models

# Create your models here.


class register_form(models.Model):
    r_user_name = models.CharField(max_length = 50)  #用户名
    r_password = models.TextField(max_length = 150)      #密码




class login_fform(models.Model):
    user_name = models.CharField(max_length = 50)  #用户名
    password = models.TextField(max_length = 150)      #密码
