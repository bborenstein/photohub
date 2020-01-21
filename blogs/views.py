from django.shortcuts import render


# Create Functions To Render html Template Files
# Allows urls.py to call views by name
def index(request):
    return render(request, 'blogs/index.html')

def portfolio(request):
    return render(request, 'blogs/portfolio.html')

def contact(request):
    return render(request, 'blogs/contact.html')