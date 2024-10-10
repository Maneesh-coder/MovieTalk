from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=9000)
    duration = models.IntegerField()
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title
