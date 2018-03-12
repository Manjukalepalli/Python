from django.conf.urls import url
from . import views           # This line is new!

print("i am in blogs urls file")
urlpatterns = [
    url(r'^display$', views.index),
    url(r'^new$',views.new),
    url(r'^create$',views.create),
    url(r'(?P<number>\d+)$',views.showblog),
    url(r'(?P<number>\d+)/edit$',views.edit),
    url(r'(?P<number>\d+)/delete$',views.delete),
    url(r'^$',views.main)
  ]