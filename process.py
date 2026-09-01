def get_film_by_id(films, id):
    for film in films:
        if(film.id == id): 
            return film
    
    return None

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