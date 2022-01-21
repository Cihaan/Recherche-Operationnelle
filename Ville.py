"""
Classe pour stocker l'identifiant, le nom, la latitude et la longitude d'une ville
"""
class Ville:
    numVille = 0
    nom = ""
    latitude = ""
    longitude = ""

    """
    Constructeur
    :param id: identifiant de la ville
    :type id: int
    :param nom: nom de la ville
    :type nom: string
    :param latitude: latitude de la ville
    :type latitude: float
    :param longitude: longitude de la ville
    :type longitude: float
    """
    def __init__(self, id, nom, latitude, longitude):
        self.numVille = id
        self.nom = nom
        self.latitude = latitude
        self.longitude = longitude
