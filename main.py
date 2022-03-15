"""
Cette partie implémente et appelle les focntions nécessaires pour effectuer les tournées
"""

from Ville import Ville
# from haversine import haversine
import math as m
import random


"""
Récupère les villes du fichier top80.txt
et les sotcke dans une structure de données de type array
"""
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

"""
Procédure pour afficher les villes contenues dans l'array
"""
def afficherVille():
    for ville in listeVilles:
        print(str(ville.numVille) + ' ' + str(ville.nom) + ' ' +
              str(ville.latitude) + ' ' + str(ville.longitude))

"""
Fonction pour calculer la distance entre deux villes
:param v1: première ville
:type v1: Ville
:param v2: deuxième ville
:type v2: Ville
:return: distance entre la ville1 et la ville2
:rtype: float
"""
def distance(v1: Ville, v2: Ville) -> float:
    # ville1 = (v1.latitude, v1.longitude)
    # ville2 = (v2.latitude, v2.longitude)

    x1 = v1.latitude * m.pi / 180
    x2 = v2.latitude * m.pi / 180
    y1 = v1.longitude * m.pi / 180
    y2 = v2.longitude * m.pi / 180

    #utilisation d'une librairie
    # distance = haversine(ville1, ville2)
    distance = abs(6371 * m.acos( (m.sin(y1) * m.sin(y2)) + (m.cos(y1) * m.cos(y2) * m.cos(x1-x2)) ))
    return distance

"""
Fonction pour créer une tournée de ville par ordre croissants des numéros de ville
:return: tournee de ville
:rtype: array[Ville]  
"""
def tourneeCroissante() -> list:
    tourneCroissante = []
    i = 1
    for ville in listeVilles:
        if(ville.numVille == i):
            tourneCroissante.append(ville)
        i += 1
    return tourneCroissante

"""
Procedure pour afficher le numero des villes de la tournée
:param tournees: array contenant les villes
:type tournees: array[Ville]
"""
def afficherTournee(tournees: Ville):
    temp = []
    for tournee in tournees:
        temp.append(tournee.numVille)
    print("tournée croissante ", temp)

"""
Fonction pour calculer la distance totale d'une tournée aller-retour
:param tournees: tournee contenant la liste des villes à visiter
:type tournees: array[Ville]
"""
def cout(tournees) -> float:
    cout = 0
    i = 0
    n = 0

    #aller
    for i in range(len(tournees)):
        cout += distance(tournees[i-1], tournees[i])
        print("itération numéro", i, cout)

    #retour
    for i in tournees:
        n -= 1
        cout += distance(tournees[n+1], tournees[n])
        print("itération numéro", n, cout)

    return cout

"""
génère une tournée aléatoire
"""
def tourAleatoire() -> list:

    tourneeDeso = tourneeCroissante()
    random.shuffle(tourneeDeso)
    
    return tourneeDeso

"""
renvoie une tournée optimisée
"""
def plusProcheVoisin(v: Ville) -> list:
    Visite = []

    #construction de la liste de ville à visiter
    for ville in listeVilles:
        if ville.viste == False:
            Visite.append(ville)
    
    tour = []
    donne(Visite, v).viste = True
    tour.append(v)

    while len(Visite) != 0:
        suivant = plusProche(Visite, v)
        
        donne(Visite, suivant).viste = True
        suivant.viste = True
        tour.append(suivant)
        Visite.remove(v)

        v = suivant

    return tour

"""
retourne la ville la plus proche
"""
def plusProche(liste, v: Ville) -> Ville:
    distanceFictive = 500
    villeProche = liste[0]

    for i in range(len(liste)):
        if liste[i].viste != True:

            tempDistance = distance(v, liste[i])

            if tempDistance < distanceFictive:
                distanceFictive = tempDistance
                dist = tempDistance
                villeProche = liste[i]
            

    return villeProche



"""
cherche ville dans liste
"""
def donne(visite: list, v: Ville) -> Ville:
    for x in visite:
        if x.numVille == v.numVille:
            return x

"""
===========================
Appelle des fonction
===========================
"""
# afficherVille()
# print("distance entre ville 1 et ville 2 : " , distance(listeVilles[0], listeVilles[1]), "km")
# afficherTournee(listeVilles)
# print(cout(listeVilles))
# print(tourAleatoire())
print(plusProcheVoisin(listeVilles[0]))