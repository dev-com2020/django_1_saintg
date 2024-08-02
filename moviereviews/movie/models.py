from django.contrib.auth.models import User
from django.db import models


class TitleStrMixin:
    def __str__(self):
        return getattr(self, 'title')


class Movie(models.Model, TitleStrMixin):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return getattr(self, 'title')


class Review(models.Model, TitleStrMixin):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()
    def __str__(self):
        return getattr(self, 'title')
