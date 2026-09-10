from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Film

def films(request):
    films = Film.objects.all()
    return render(request, "app/films.html", {"films": films})