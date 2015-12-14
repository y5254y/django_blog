from django.contrib import admin
from .models import BlogPost
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
	#fields = ['title','timestamp']
	list_display = ('title','timestamp')
admin.site.register(BlogPost, BlogPostAdmin)