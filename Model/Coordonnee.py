# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(num_ligne: int, num_colonne: int) -> tuple:
    """
    Créer une coordonnée sous forme de tuple à partir d'un numéro de ligne et de colonne.

    Cette fonction renvoie un tuple sous la forme (num_ligne, num_colonne)

    :param num_ligne: entier positif représentant numéro de ligne
    :param num_colonne: entier positif représentant le numéro de colonne
    :return: tuple (num_ligne, num colonne)
    """

    # Test si le numéro de ligne et numéro de colonne sont des entiers
    if type(num_ligne) != int or type(num_colonne) != int :
        raise TypeError(f"construireCoordonnee : Le numéro de ligne {type(num_ligne)} ou le numéro de colonne {type(num_colonne)} ne sontpas des entiers")
    # Test si le numéro de ligne ou de colonnes sont positif
    elif num_ligne < 0 or num_colonne < 0 :
        raise ValueError(f"construireCoordonnee : Le numéro de ligne {num_ligne} ou de colonne {num_colonne} ne sont pas positifs.")

    return (num_ligne, num_colonne)


def getLigneCoordonnee(coord: tuple) -> int:
    """
    Récupère le numéro de ligne de la coordonnée.

    :param coord: tuple conforme à une coordonnée
    :return: entier représentant le numéro de ligne
    """
    # Test si la coordonnée est conforme
    if type_coordonnee(coord) != True :
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")

    return coord[0]


def getColonneCoordonnee(coord: tuple) -> int:
    """
    Récupère le numéro de colonne de la coordonnée.

    :param coord: tuple conforme à une coordonnée
    :return: entier représentant le numéro de colonne
    """
    # Test si la coordonnée est conforme
    if type_coordonnee(coord) != True :
        raise TypeError("getColonneCoordonnee : Le paramètre n’est pas une coordonnée")

    return coord[1]

