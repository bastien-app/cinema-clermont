from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length = 255)
    director = models.CharField(max_length = 255)


class Cinema(models.Model):
    name = models.CharField(max_length = 255)

class Seance(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    seance_date = models.DateTimeField()
    lang = models.CharField(max_length = 15)
    techno = models.CharField(max_length = 15)