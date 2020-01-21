from django.shortcuts import render

def index(request):
    return render(request, 'blogs/index.html')

def about(request):
    return render(request, 'blogs/about.html')

def contact(request):
    return render(request, 'blogs/contact.html')