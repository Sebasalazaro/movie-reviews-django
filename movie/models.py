from django.db import models

class Movie(models.Model):
    """Movie model for storing film information.
    
    Attributes:
        title: Movie title
        description: Brief movie description
        image: Movie poster image
        url: Optional external URL for more information
        genre: Movie genre(s)
        year: Release year
    """
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = 'movie/images/')
    url = models.URLField(blank = True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title