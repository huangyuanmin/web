# _*_ coding: utf-8 _*_

from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from apps.login.models import register_form
from apps.login.models import login_fform

# Create your views here.




def register(request):
    if request.method == 'POST':
        registerforms = register_form(request.POST)
        if registerforms.is_valid():
            r_user_name = registerforms.cleaned_data['r_user_name']
            r_password = registerforms.cleaned_data['r_password']


            register_form.objects.create(r_user_name=r_user_name,r_password=r_password)
            register_form.save()

            return HttpResponse('regist success!!!')
    else:
        registerforms = register_form()
    return render('login_form',{'registerforms':registerforms})


def login(request):
    if request.method == 'POST':
        loginforms = login_fform(request.POST)
        if loginforms.is_valid():
            user_name = loginforms.cleaned_data['user_name']
            password = loginforms.cleaned_data['password']

            login = login_fform.objects.filter(username__exact=user_name,password__exact=password)

            if login:
                return render(request,'main.html',{'loginforms':loginforms})
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        loginforms = login_fform() #表单实例化
    return render(request,'login.html',{'loginforms':loginforms})