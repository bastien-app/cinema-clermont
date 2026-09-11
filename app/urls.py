from django.urls import path
from . import views

urlpatterns = [
    path("films/", views.films),
    path("films/<int:film_id>/", views.film_detail)
]