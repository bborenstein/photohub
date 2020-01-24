from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Posting
from django.core.paginator import EmptyPage, PageNotAnInteger, PageNotAnInteger

from .models import Posting

def index(request):

    # Fetching All Data (DB Objects/Media)
    postings = Posting.objects.all()

    # Create Pagination
    paginator = Paginator(postings, 3)
    page = request.GET.get('page')
    paged_postings = paginator.get_page(page)

    # Declaring Data as Context Var for Looping in HTML/View
    context = {
        'postings': paged_postings
    }

    # Context Must Be Passed Into Render Function 
    return render(request, 'postings/postings.html', context)

def posting(request, posting_id):
 
    # Fetching Single Postings Based On PK (DB Primary Key) ID
    posting = get_object_or_404(Posting, pk=posting_id)

    # Declaring Data Var As Single ID
    context = {
        'posting': posting_id
    }

    return render(request, 'postings/posting.html', context)

# Must Pass In 'posting_id' As Parameter 
#def posting(request, posting_id): 
#    return render(request, 'postings/posting.html')