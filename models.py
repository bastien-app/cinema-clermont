class Film:
    def __init__(self, id, title, director):
        self.id = id
        self.title = title
        self.director = director

class Cinema:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Seance:
    def __init__(self, id_film, id_cinema, seance_date, lang, techno):
        self.id_film = id_film
        self.id_cinema = id_cinema
        self.seance_date = seance_date
        self.lang = lang
        self.techno = techno
    
    def __str__(self):
        return f'Séance du {self.seance_date} en {self.lang} {self.techno}'