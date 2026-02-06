from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

def home(request):
    """Display all movies with optional search functionality.
    
    Args:
        request: HTTP request object containing optional 'searchMovie' parameter
        
    Returns:
        Rendered home.html template with movies list and search term
    """
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains = searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm':searchTerm , 'movies':movies}, )
    
def about(request):
    """Display the about page."""
    return render(request, 'about.html')

def signup(request):
    """Display signup page with optional email parameter.
    
    Args:
        request: HTTP request object containing optional 'email' parameter
        
    Returns:
        Rendered signup.html template with email if provided
    """
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})

def statistics_view(request):
    """Generate and display movie statistics charts.
    
    Creates two bar charts:
    - Number of movies per year
    - Number of movies per genre
    
    Returns:
        Rendered statistics.html template with base64-encoded chart images
    """
    # Chart: Number of movies by year
    matplotlib.use('Agg')
    all_movies = Movie.objects.all()
    movie_counts_by_year = {}

    for movie in all_movies:
        year = movie.year if movie.year else "None"
        if year in movie_counts_by_year:
            movie_counts_by_year[year] += 1
        else:
            movie_counts_by_year[year] = 1

    bar_width = 0.5
    bar_positions = range(len(movie_counts_by_year))

    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width , align='center')

    plt.title('Movie per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)

    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    # Chart: Number of movies by genre
    movie_counts_by_genre = {}

    for movie in all_movies:
        genre = movie.genre if movie.genre else "None"
        if genre in movie_counts_by_genre:
            movie_counts_by_genre[genre] += 1
        else:
            movie_counts_by_genre[genre] = 1

    bar_width2 = 0.5
    bar_positions2 = range(len(movie_counts_by_genre))

    plt.bar(bar_positions2, movie_counts_by_genre.values(), width=bar_width2 , align='center')

    plt.title('Movie per genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions2, movie_counts_by_genre.keys(), rotation=90)

    plt.subplots_adjust(bottom=0.3)

    buffer2 = io.BytesIO()
    plt.savefig(buffer2, format='png')
    buffer2.seek(0)
    plt.close()

    image_png2 = buffer2.getvalue()
    buffer2.close()
    graphic2 = base64.b64encode(image_png2)
    graphic2 = graphic2.decode('utf-8')

    return render(request, 'statistics.html',{'graphic': graphic, 'graphic2': graphic2})