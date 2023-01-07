# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)

def isContenuCorrect(content: int) -> bool:
    """
    Cette fonction vérifie si un entier peut représenter le contenu d'une cellule
    :param content: entier
    :return: True si l'entier est entre 0 et 8 ou s'il vaut la valeur de const.ID_MINE
    """
    if type(content) != int :
        ret = False
    else :
        ret = ( content <= 8 and content >= 0 ) or content == const.ID_MINE

    return ret

def construireCellule(content: int = 0, visible: bool = False) -> dict :
    """
    Cette fonction créer une cellule à partir d'un entier et d'un booléen.

    :param content: entier représentant le contenu de la cellule
    :param visible: booléen donnant la visibilité de la cellule
    :return: cellule final sous forme d'un dictionnaire
    """
    if isContenuCorrect(content) != True :
        raise ValueError(f"construireCellule : le contenu {content} n'est pas correct")
    if type(visible) != bool :
        raise TypeError(f"onstruireCellule : le contenu {visible} n'est pas un booléen")

    return { const.CONTENU : content, const.VISIBLE : visible } 