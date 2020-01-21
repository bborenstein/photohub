from django.urls import path
from . import views
 
# Blogs URL Directory
## Imports to Django URLS
urlpatterns = [
    # name is Django easy internal ref
    path('', views.index, name='index'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
]