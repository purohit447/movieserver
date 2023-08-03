from django.db import models

# Create your models here.
class data(models.Model):
    movie_id = models.CharField(max_length=20, unique=True)
    posterlink = models.CharField(max_length=50)
    seriestitle = models.CharField(max_length=50)
    releasedyear = models.CharField(max_length=5)
    certification = models.CharField(max_length=5)
    runtime = models.CharField(max_length=10)
    genre = models.CharField(max_length=30)
    IMDBrating = models.CharField(max_length=4)
    overview = models.CharField(max_length=100)
    metascore = models.CharField(max_length=5)
    Director = models.CharField(max_length=20)
    star1 = models.CharField(max_length=20)
    star2 = models.CharField(max_length=20)
    star3 = models.CharField(max_length=20)
    star4 = models.CharField(max_length=20)
    noofvotes = models.CharField(max_length=10)
    gross = models.CharField(max_length=20)

    def __str__(self):
        return self.movie_id
    
    