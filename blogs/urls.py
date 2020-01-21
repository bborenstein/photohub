from django.urls import path

# Import Views to use simple names
from . import views
 
# Blogs URL Directory

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
]