from django.conf.urls import url
from .import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', views.archive, name='archive'),


]
