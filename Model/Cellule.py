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

    return { const.CONTENU : content, const.VISIBLE : visible, const.ANNOTATION : None }

def getContenuCellule(cellule: dict) -> int :
    """
    Cette fonction récupère le contenu d'une cellule

    :param cellule: dictionnaire représentant la cellule
    :return: entier étant le contenu de la cellule
    """
    if type_cellule(cellule) != True :
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule")
    return cellule[const.CONTENU]

def isVisibleCellule(cellule : dict) -> bool :
    """
    Cette fonction vérifie if a cellule est visible ou non

    :param cellule: dictionnaire représentant une cellule
    :return: True si la cellule est visible, False si elle ne l'est pas
    """
    if type_cellule(cellule) != True :
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule")

    return cellule[const.VISIBLE]

def setContenuCellule(cellule: dict, content: int) -> None:
    """
    Cette fonction permet de modifier le contenu d'une cellule déjà existante

    :param cellule: dictionnaire représentant une cellule
    :param content: Un entier entre 0 et 8 inclus ou ayant la valeur de const.ID_MINE
    :return: La fonction ne renvoie rien
    """

    if type(content) != int :
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    if content > 8 or content < 0 and content != const.ID_MINE:
        raise ValueError(f"setContenuCellule : la valeur du contenu {content} n’est pas correcte.")
    if type_cellule(cellule) != True :
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")

    cellule[const.CONTENU] = content

    return None

def setVisibleCellule(cellule: dict, visible: bool) -> None :
    """
    Cette fonction permet de modifier la visibilité d'une cellule déjà éxistante

    :param cellule: dictionnaire représentant une cellule
    :param visible: booléen donnant la visibilité de la cellule
    :return: Rien
    """
    if type_cellule(cellule) != True :
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    if type(visible) != bool :
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen")
    cellule[const.VISIBLE] = visible

    return None

def contientMineCellule(cellule: dict) -> bool :
    """
    Cette fonction permet de vérifier si contient une mine ou non

    :param cellule: dictionnaire représentant une cellule
    :return: True si la cellule contient une mine, False si la cellule n'en contient pas
    """
    if type_cellule(cellule) != True :
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule")

    return cellule[const.CONTENU] == const.ID_MINE

def isAnnotationCorrecte(annotation: str) -> bool:
    """
    Cette fonction reçois une annotation et vérifie si elle est correcte
    :param annotation: chaine de caractère
    :return: True si elle vaut None, const.FLAG ou const.DOUTE, sinon False
    """
    return annotation in [None, const.FLAG, const.DOUTE]


def getAnnotationCellule(cellule: dict) -> str:
    """
    Cette fonction récupère l'annotation d'une cellule.

    :param cellule: dictionnaire de type cellule
    :return: chaîne de carractère stocké comme annotation par la cellule
    """
    if type_cellule(cellule) != True :
        raise TypeError("getAnnotationCellule : le paramètre valeur_du paramètre n’est pas une cellule")
    if const.ANNOTATION not in cellule :
        ret = None
    else :
        ret = cellule[const.ANNOTATION]
    return ret

def changeAnnotationCellule(cellule: dict) -> None:
    """
    Cette fonction change l'annotation d'une cellule

    :param cellule: dictionnaire de type cellule
    :return: rien
    """
    if type_cellule(cellule) != True:
        raise TypeError("changeAnnotationCellule : le paramètre n’est pas une cellule")

    if cellule[const.ANNOTATION] == None :
        ret = const.FLAG
    elif cellule[const.ANNOTATION] == const.FLAG :
        ret = const.DOUTE
    else :
        ret = None
    cellule[const.ANNOTATION] = ret

    return None