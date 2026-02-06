from django.shortcuts import render
from .models import News

def news(request):
    """Display all news articles ordered by date (newest first).
    
    Returns:
        Rendered news.html template with news articles list
    """
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})

