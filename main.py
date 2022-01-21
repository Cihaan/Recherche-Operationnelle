from cmath import acos
from sqlalchemy import null
from Ville import Ville
import math
# Récupération des Villes de puis le fichier
f = open("./instances/ListeComplete.txt", "r")
lines = f.readlines()
listeVilles = []
for line in lines:
    # parse des lignes
    ville = line.split(" ")
    ville[3].rstrip("\n")

    # création ville
    city = Ville(int(ville[0]), ville[1], float(ville[2]), float(ville[3]))

    # ajout à la liste de ville la ville
    listeVilles.append(city)
f.close()


# Affichage des villes
def afficherVille():
    for ville in listeVilles:
        print(ville.numVille)
        print(ville.nom)
        print(ville.latitude)
        print(ville.longitude)


def distance(v1: Ville, v2: Ville) -> float:
    r = 6371
    x1 = math.radians(v1.longitude)
    x2 = math.radians(v2.longitude)
    y1 = math.radians(v1.latitude)
    y2 = math.radians(v2.latitude)
    distance = abs(r * math.acos((math.sin(y1) * math.sin(y2)) +
                                  (math.cos(y1) * math.cos(y2) * math.cos(x1 - x2)) ))

    return distance


# appel des fonctions
# afficherVille()
print("distance entre les deux villes : " +
      str(distance(listeVilles[0], listeVilles[1])))
