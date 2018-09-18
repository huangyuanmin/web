from django.contrib import admin
from main.models import BlogsPost
from main.models import BlogPost
from main.models import BloPost
from main.models import BlPost


# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'timestamp']

class BlogPostAdmin(admin.ModelAdmin):
    list1_display = ['title1', 'body1', 'timestamp1']

class BloPostAdmin(admin.ModelAdmin):
    list2_display = ['title2', 'body2', 'timestamp2']

class BlPostAdmin(admin.ModelAdmin):
    list3_display = ['title3', 'body3', 'timestamp3']






admin.site.register(BlogsPost, BlogsPostAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BloPost, BloPostAdmin)
admin.site.register(BlPost, BlPostAdmin)
