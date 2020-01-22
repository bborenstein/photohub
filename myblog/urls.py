from django.contrib import admin
from django.urls import path, include
# Import Settings Containing URL/ROOT Vars
## MEDIA_ROOT Will Set photos/media in '/' Folder
from django.conf import settings
# Imports Static Media
from django.conf.urls.static import static

# Base URL Directory 
urlpatterns = [
    path('', include('blogs.urls')),
    path('postings/', include('postings.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
