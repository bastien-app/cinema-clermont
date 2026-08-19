import datetime

class Film:
    def __init__(self, id, title, director):
        self.id = id
        self.title = title
        self.director = director


film1 = Film(1, "Avatar", "Someone")
film2 = Film(2, "Avatar 2", "Someone")
film3 = Film(3, "Avatar 3", "Someone")

films = [film1, film2, film3]

def get_film_by_id(films, id):
    for film in films:
        if(film.id == id): 
            return film
    
    return None




class Cinema:
    def __init__(self, id, name):
        self.id = id
        self.name = name


pathe_aubiere = Cinema(1, "Pathé Aubière")
cgr_le_paris = Cinema(2, "CGR Le Paris")

cinemas = [pathe_aubiere, cgr_le_paris]

class Seance:
    def __init__(self, id_film, id_cinema, seance_date, lang, techno):
        self.id_film = id_film
        self.id_cinema = id_cinema
        self.seance_date = seance_date
        self.lang = lang
        self.techno = techno
    
    def __str__(self):
        return f'Séance du {self.seance_date} en {self.lang} {self.techno}'


seance_avatar = Seance(film1.id, pathe_aubiere.id, datetime.datetime(2026, 8, 18, 17, 30), "vf", "2D")
seance2 = Seance(film1.id, pathe_aubiere.id, datetime.datetime(2026, 8, 18, 22, 00), "vf", "3D")
seance3 = Seance(film1.id, cgr_le_paris.id, datetime.datetime(2026, 8, 22, 21, 30), "vostfr", "2D")
seance4 = Seance(film2.id, pathe_aubiere.id, datetime.datetime(2026, 8, 18, 20, 00), "vf", "IMAX")
seance5 = Seance(film3.id, cgr_le_paris.id, datetime.datetime(2026, 8, 18, 20, 45), "vo", "2D")

seances = [seance_avatar, seance2, seance3, seance4, seance5]

def get_cinema_by_id(cinemas, id):
    for cine in cinemas:
        if(cine.id == id): 
            return cine
    
    return None



def get_seance_info(seance, films, cinemas):
    film = get_film_by_id(films, seance.id_film)
    cinema = get_cinema_by_id(cinemas, seance.id_cinema)

    infos = {"Title": film.title, "Cinema": cinema.name, "Date": seance.seance_date, "Language": seance.lang, "Techno" : seance.techno}

    return infos




def get_seances_by_film(id, seances):
    seances_du_film = []
    
    for seance in seances: 
        if(seance.id_film == id):
            seances_du_film.append(seance)
    
    return seances_du_film


seances_avatar = get_seances_by_film(1, seances)

for seance in seances_avatar:
    print(seance)