from django.shortcuts import render
from django.http import HttpResponse
# Import Posting & Photographer Models To Bring In Data To Contact Us (Photographers) & Home/Index (Featured Posts)
from postings.models import Posting
from photographers.models import Photographer

# Create Functions To Render html Template Files
def index(request):
    # [:3] Limits Featured To Only Most Recent 3 Postings
    postings = Posting.objects.order_by('-posted_date').filter(is_published=True)[:3]
    # Fetch Schema Data (Postings) As Variable 'context'
    context = {
        'postings': postings
    }
    L
    return render(request, 'blogs/index.html', context)

def contact(request):
    # Get All Photographers In Database
    photographers = Photographer.objects.order_by('-hire_date')

    context = {
        'photographers': photographers
    }

    return render(request, 'blogs/contact.html', context)