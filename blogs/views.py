from django.shortcuts import render


def index(request):
    return render(request, 'blogs/index.html')

def portfolio(request):
    return render(request, 'blogs/portfolio.html')

def contact(request):
    return render(request, 'blogs/contact.html')