from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.shortcuts import render
from .models import Film, Seance, Cinema

def films(request):
    films = Film.objects.all()
    return render(request, "app/films.html", {"films": films})

def film_detail(request, film_id):
    film = Film.objects.get(id = film_id)
    seances = Seance.objects.filter(film = film)
    cinemas = Cinema.objects.filter(seance__film = film).distinct()
    return render(request, "app/film_detail.html", {"film": film, "seances": seances, "cinemas": cinemas})