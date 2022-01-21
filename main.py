from Ville import Ville
from haversine import haversine
import math as m

# Récupération des Villes de puis le fichier
f = open("./instances/top80.txt")
# récupère les lignes du doc txt
lines = f.readlines()
listeVilles = []
for line in lines:
    # parse des lignes
    ville = line.split(" ")
    ville[3] = ville[3].strip('\n')

    # création ville
    city = Ville(int(ville[0]), ville[1], float(ville[2]), float(ville[3]))

    # ajout à la liste de ville la ville
    listeVilles.append(city)
f.close()


# Affichage des villes
def afficherVille():
    for ville in listeVilles:
        print(str(ville.numVille) + ' ' + str(ville.nom) + ' ' +
              str(ville.latitude) + ' ' + str(ville.longitude))


# calcule la distance entre deux villes
def distance(v1: Ville, v2: Ville) -> float:
    ville1 = (v1.latitude, v1.longitude)
    ville2 = (v2.latitude, v2.longitude)

    distance = haversine(ville1, ville2)
    return distance


# créer une tournée de ville par ordre croissants des numéros de ville
def tourneeCroissante():
    tourneCroissante = []
    i = 1
    for ville in listeVilles:
        if(ville.numVille == i):
            tourneCroissante.append(ville)
        i += 1
    return tourneCroissante


# affiche le numero des villes de la tournée passée en paramètre
def afficherTournee(tournees: Ville):
    temp = []
    for tournee in tournees:
        temp.append(tournee.numVille)
    print("tournée croissante ", temp)


# calcule la distance totale d'une tournée
def cout(tournees) -> float:
    cout = 0
    i = 0

    for i in range(len(tournees)):
        if(i < (len(tournees)-1)):
            cout += distance(tournees[i], tournees[i+1])
            print("itération numéro", i, cout)
        else:
            return cout

    return cout


## Appel des fonctions ##
# afficherVille()
# print("distance entre ville 1 et ville 2 : " , distance(listeVilles[0], listeVilles[1]), "km")
# afficherTournee(listeVilles)
# print(cout(listeVilles))