from django.db import models


# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)  # 博客标题
    body = models.TextField()                   # 博客正文
    timestamp = models.DateTimeField()          # 创建时间

class BlogPost(models.Model):
    title1 = models.CharField(max_length = 150)  # 博客标题
    body1 = models.TextField()                   # 博客正文
    timestamp1 = models.DateTimeField()          # 创建时间

class BloPost(models.Model):
    title2 = models.CharField(max_length = 150)  # 博客标题
    body2 = models.TextField()                   # 博客正文
    timestamp2 = models.DateTimeField()          # 创建时间

class BlPost(models.Model):
    title3= models.CharField(max_length = 150)  # 博客标题
    body3 = models.TextField()                   # 博客正文
    timestamp3 = models.DateTimeField()          # 创建时间


