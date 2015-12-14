from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from  .models import BlogPost
# Create your views here.

def archive(request):
	posts = BlogPost.objects.all()
	template = loader.get_template('blog/archive.html')
	context = RequestContext(request, {'posts':posts})
	return HttpResponse(template.render(context))
