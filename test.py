import process 
import data 

seances_avatar = process.get_seances_by_film(1, data.seances)

for seance in seances_avatar:
    print(seance)


infos = process.get_seance_info(data.seance3, data.films, data.cinemas)

print(infos)