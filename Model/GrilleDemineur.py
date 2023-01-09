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


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    """
    Vérifie si une coordonnée est présente dans une grille

    :param grille: liste conforme à une grille de démineur
    :param coord: tuple représentant une coordonée dans la grille
    :return: True si la coordonnée est dans la grille, False si elle ne l'est pas
    """
    if type_grille_demineur(grille) != True or type(coord) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")

    estCoord = True
    if coord[0] >= getNbLignesGrilleDemineur(grille) or coord[1] >= getNbColonnesGrilleDemineur(grille) or coord[0] < 0 or coord[1] < 0:
        estCoord = False
    return estCoord

def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    """
    Cette fonction cherche une cellule dans une grille à la coordonnée donné.
    :param grille: liste conforme à une grile de démineur
    :param coord: tuple conforme à une coordonnée
    :return: La cellule à la coordonnée coord de la grille
    """
    if type_grille_demineur(grille) != True or type_coordonnee(coord) != True:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille, coord) != True:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille")

    return grille[coord[0]][coord[1]]

def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    """
    Cette fonction récupère le contenu d'une cellule à une dite coordonée dans une grille

    :param grille: liste conforme à une liste de démineur
    :param coord: tuple conforme à une coordonnée
    :return: entier représentant le contenu d'une cellule à la coordonnée coord de la grille
    """

    return getCelluleGrilleDemineur(grille, coord)[const.CONTENU]

def setContenuGrilleDemineur(grille: list, coord: tuple, content: int) -> None:
    """
    Cette fonction le contenu d'une cellulde d'une grille de démineur

    :param grille: liste conforme à une liste de démineur
    :param coord: tuple conforme à une coordonnée
    :param content: entier conforme au contenu d'une cellule
    :return: rien
    """
    isCoordonneeCorrecte(grille, coord)
    isContenuCorrect(content)

    setContenuCellule(grille[coord[0]][coord[1]], content)

    return None

def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Cette fonction renvoi le paramètre de visibilité d'une cellule d'une grille

    :param grille: liste conforme à une liste de démineur
    :param coord: tuple conforme à une coordonnée
    :return: True si la cellule est visible, sinon False
    """
    isCoordonneeCorrecte(grille, coord)

    return grille[coord[0]][coord[1]][const.VISIBLE]

def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    """
    Cette fonction change le paramètre de visibilité d'une cellule de la grille

    :param grille: liste conforme à une liste de démineur
    :param coord: tuple conforme à une coordonnée
    :param visible:
    :return:
    """
    isCoordonneeCorrecte(grille, coord)

    setVisibleCellule(grille[coord[0]][coord[1]], visible)

    return None

def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Cette fonction vérifie si la cellule de la grille est une Mine ou non

    :param grille: liste conforme à une liste de démineur
    :param coord: tuple conforme à une coordonnée
    :return: True sir la cellule contient une mine, sinon False
    """

    isCoordonneeCorrecte(grille, coord)
    return contientMineCellule(grille[coord[0]][coord[1]])

def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    """
    Cette fonction récupère les coordonnées des celulles voisines d'une cellule donnée

    :param grille: liste conforme à une liste de démineur
    :param coord: tuple conforme à une coordonnée
    :return: liste des coordonées des cellules voisines
    """
    if type_grille_demineur(grille) != True or type(coord) != tuple :
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille, coord) == False :
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")

    h = coord[0]
    v = coord[1]

    voisins = []
    for i in range(h-1, h+2):
        for j in range(v-1, v+2):
            if isCoordonneeCorrecte(grille, (i, j)) and (i, j) != coord:
                voisins.append((i, j))
    return voisins

def placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple) -> None:
    """
    Cette fonction place les mines sur la grille

    :param grille: grille du démineur
    :param nb: nombre de mines à placer
    :param coord: Coordonnée du premier clic, qui ne peut pas avoir de mine
    :return: rien
    """

    if nb < 0 or nb >= getNbColonnesGrilleDemineur(grille) * getNbLignesGrilleDemineur(grille) :
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorect")
    if isCoordonneeCorrecte(grille, coord) == False :
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille")
    lignes = getNbLignesGrilleDemineur(grille)
    cols = getNbColonnesGrilleDemineur(grille)

    for i in range(nb):
        x = randint(0, lignes - 1)
        y = randint(0, cols - 1)
        while getContenuCellule(grille[x][y]) == const.ID_MINE or (x == coord[0] and y == coord[1]) :
            x = randint(0, lignes - 1)
            y = randint(0, cols - 1)


        setContenuCellule(grille[x][y], const.ID_MINE)

    compterMinesVoisinesGrilleDemineur(grille)

    return None

def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    """
    Cette fonction ajoute pour chaque cellule le nombre de mine autour

    :param grille: grille de démineur
    :return: rien
    """
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if getContenuCellule(grille[i][j]) != -1:
                voisins = getCoordonneeVoisinsGrilleDemineur(grille, (i, j))
                for k in range(len(voisins)):
                    cell = voisins[k]
                    if getContenuCellule(grille[cell[0]][cell[1]]) == -1 :
                        setContenuCellule(grille[i][j], getContenuCellule(grille[i][j])+1)
    return None


def getNbMinesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction renvoie le nombre de mines contenues dans la liste

    :param grille: grille du démineur
    :return: nombre entier de mines dans la grille
    """
    if type_grille_demineur(grille) != True:
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")

    compte = 0
    for ligne in grille:
        for cellule in ligne :
            if cellule[const.CONTENU] == const.ID_MINE:
                compte += 1
    return compte

def getAnnotationGrilleDemineur(grille: list, coord: tuple) -> str:
    """
    Cette fonction récupère l'annotation d'une cellule de la grille.

    :param grille: grille du démineur
    :param coord: coordonnées de la cellule
    :return: Annotation de la cellule
    """
    return getAnnotationCellule(grille[coord[0]][coord[1]])

def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction compte le nombre de mines à marquer

    :param grille: grille du démineur
    :return: le nombre de mines totales moins le nombre de cellules marquées
    """
    compte = 0
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if getAnnotationGrilleDemineur(grille, (i, j)) == const.FLAG :
                compte += 1
    return getNbMinesGrilleDemineur(grille) - compte

def gagneGrilleDemineur(grille: list) -> bool:
    """
    La fonction vérifie si la partie est gagnée ou non

    :param grille: grille du démineur
    :return: True si la partie est gagnée, False sinon
    """
    gagner = True
    for ligne in grille :
        for case in ligne :
            if getContenuCellule(case) != const.ID_MINE and isVisibleCellule(case) != True :
                gagner = False
            elif getContenuCellule(case) == const.ID_MINE and isVisibleCellule(case) == True :
                gagner = False
            elif getContenuCellule(case) == const.ID_MINE and isVisibleCellule(case) == False and getAnnotationCellule(case) != const.FLAG :
                gagner = False
    return gagner

def perduGrilleDemineur(grille: list) -> bool:
    """
    Cette fonction vérifie si une partie est perdue

    :param grille: grille du démineur
    :return: True si la partie est perdue, False sinon
    """
    perdu = False
    for ligne in grille :
        for case in ligne :
            if getContenuCellule(case) == const.ID_MINE and isVisibleCellule(case) == True :
                perdu = True
    return perdu