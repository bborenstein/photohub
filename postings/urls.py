from django.urls import path

# Import Views to use simple names
from . import views
 
# Postings URL Directory

urlpatterns = [
    path('', views.index, name='postings'),
    path('<int:posting_id>', views.posting, name='posting'),
]

