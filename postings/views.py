from django.shortcuts import render

from .models import Posting

def index(request):

    # Grabbing All Data (DB Objects/Media)
    postings = Posting.objects.all()

    # Declaring Data as Context Var for Looping in HTML/View
    context = {
        'postings': postings
    }

    # Context Must Be Passed Into Render Function 
    return render(request, 'postings/postings.html', context)

# Must Pass In 'posting_id' As Parameter 
def posting(request, posting_id): 
    return render(request, 'postings/posting.html')