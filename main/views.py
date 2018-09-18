from django.shortcuts import render
from django.http import HttpResponse
from main.models import BlogPost


# Create your views here.

def Index(request):
    return render(request,'main.html',)  # 返回main.html页面

def blog_index(request):
    blog_list = BlogPost.objects.all()  # 获取所有数据
    return render(request,'main.html', {'blog_list':blog_list})   # 返回index.html页面



