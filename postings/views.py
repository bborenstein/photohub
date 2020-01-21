from django.shortcuts import render

from . import views

def index(request):
    return render(request, 'postings/postings.html')

def posting(request):
    return render(request, 'postings/posting.html')