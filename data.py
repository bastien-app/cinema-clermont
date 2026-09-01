import datetime
from models import Film, Cinema, Seance

film1 = Film(1, "Avatar", "Someone")
film2 = Film(2, "Avatar 2", "Someone")
film3 = Film(3, "Avatar 3", "Someone")

films = [film1, film2, film3]

pathe_aubiere = Cinema(1, "Pathé Aubière")
cgr_le_paris = Cinema(2, "CGR Le Paris")

cinemas = [pathe_aubiere, cgr_le_paris]

seance_avatar = Seance(film1.id, pathe_aubiere.id, datetime.datetime(2026, 8, 18, 17, 30), "vf", "2D")
seance2 = Seance(film1.id, pathe_aubiere.id, datetime.datetime(2026, 8, 18, 22, 00), "vf", "3D")
seance3 = Seance(film1.id, cgr_le_paris.id, datetime.datetime(2026, 8, 22, 21, 30), "vostfr", "2D")
seance4 = Seance(film2.id, pathe_aubiere.id, datetime.datetime(2026, 8, 18, 20, 00), "vf", "IMAX")
seance5 = Seance(film3.id, cgr_le_paris.id, datetime.datetime(2026, 8, 18, 20, 45), "vo", "2D")

seances = [seance_avatar, seance2, seance3, seance4, seance5]