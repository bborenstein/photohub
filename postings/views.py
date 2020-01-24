from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Posting

# Fetching All Data (DB Objects/Media)
def index(request):

    postings = Posting.objects.all()

    # Create Pagination
    #paginator = Paginator(postings, 2)
    #page = request.GET.get('page')
    #paged_postings = paginator.get_page(page)

    context = {
        'postings': postings
    }

    # Context Must Be Passed Into Render Function 
    return render(request, 'postings/postings.html', context)

# Function Fetches Individual Postings
def posting(request, posting_id):
 
    posting = get_object_or_404(Posting, pk=posting_id)

    context = {
        'posting': posting
    }

    return render(request, 'postings/posting.html', context)
