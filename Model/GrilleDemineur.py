# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(nb_ligne: int, nb_col: int) -> list:
    """
    Cette fonction construit une grille à partir d'un nombre de colonne et de ligne entrés

    :param nb_ligne: entier représentant le nombre de ligne
    :param nb_col: entier représentant le nombre de colonne
    :return: liste représentant la grille
    """
    if nb_ligne <= 0 or nb_col <= 0 :
        raise ValueError(f"onstruireGrilleDemineur : Le nombre de lignes {nb_ligne} ou de colonnes {nb_col} est négatif ou nul")
    if type(nb_col) != int or type(nb_ligne) != int :
        raise TypeError(f" construireGrilleDemineur : Le nombre de lignes {nb_ligne} ou de colonnes {nb_col} n’est pas un entier.")

    grille = []
    for i in range(nb_ligne):
        grille.append([])
        for j in range(nb_col):
            grille[i].append(construireCellule())

    return grille

def getNbLignesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction récupère le nombre de ligne d'une grille de démineur.

    :param grille: liste conforme à une grille de démineur
    :return: entier représentant le nombre de ligne de la grille
    """
    if type_grille_demineur(grille) != True:
        raise TypeError(f"getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)

def getNbColonnesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction récupère le nombre de ligne d'une grille de démineur.

    :param grille: liste conforme à une grille de démineur
    :return: entier représentant le nombre de colonnes d'une grille
    """
    if type_grille_demineur(grille) != True:
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])