import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from datetime import datetime
from django.utils import timezone

from app.models import Film, Cinema, Seance


# Films
avatar = Film.objects.create(
    title="Avatar",
    director="Someone"
)

avatar2 = Film.objects.create(
    title="Avatar 2",
    director="Je sais pas"
)

avatar3 = Film.objects.create(
    title="Avatar 3",
    director="Je sais pas"
)


# Cinémas
pathe = Cinema.objects.create(
    name="Pathé Aubière"
)

cgr = Cinema.objects.create(
    name="CGR Le Paris"
)


# Séances
Seance.objects.create(
    film=avatar,
    cinema=pathe,
    seance_date=timezone.make_aware(datetime(2026, 8, 18, 17, 30)),
    lang="VF",
    techno="2D"
)

Seance.objects.create(
    film=avatar,
    cinema=pathe,
    seance_date=timezone.make_aware(datetime(2026, 8, 18, 22, 0)),
    lang="VF",
    techno="3D"
)

Seance.objects.create(
    film=avatar,
    cinema=cgr,
    seance_date=timezone.make_aware(datetime(2026, 8, 22, 21, 30)),
    lang="VOSTFR",
    techno="2D"
)

Seance.objects.create(
    film=avatar2,
    cinema=pathe,
    seance_date=timezone.make_aware(datetime(2026, 8, 18, 20, 0)),
    lang="VF",
    techno="IMAX"
)

Seance.objects.create(
    film=avatar3,
    cinema=cgr,
    seance_date=timezone.make_aware(datetime(2026, 8, 18, 20, 45)),
    lang="VO",
    techno="2D"
)

print("Données de test créées avec succès !")