from django.conf.urls import url
from . import views           # This line is new!

print("i am in blogs urls file")
urlpatterns = [
    url(r'^$',views.main)
  ]