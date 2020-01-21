from django.contrib import admin
from django.urls import path, include

# Base URL Directory 
urlpatterns = [
    path('', include('blogs.urls')),
    path('postings/', include('postings.urls')),
    path('admin/', admin.site.urls),
]
