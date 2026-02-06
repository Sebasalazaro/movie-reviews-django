from django.db import models

class News(models.Model):
    """News article model for storing movie-related news.
    
    Attributes:
        headline: News article title
        body: Full article text
        date: Publication date
    """
    headline = models.CharField(max_length = 200)
    body = models.TextField()
    date = models.DateField()

    def __str__(self): return self.headline
    
