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

    :param content: entier représentant un contenu
    :return: True si le contenu est entre 0 et 8 ou s'il vaut la valeur de const.ID_MINE
    """

    # Vérifie que le contenu soit bien un entier
    # si content ne l'est pas, ret vaudra False
    if type(content) != int :
        ret = False
    # Sinon attribue le résultat du test de conformité de contenu
    # sur content à la variable ret
    else :
        ret = ( content <= 8 and content >= 0 ) or content == const.ID_MINE

    return ret


def construireCellule(content: int = 0, visible: bool = False) -> dict :
    """
    Cette fonction créer une cellule à partir d'un entier et d'un booléen.

    :param content: entier confrome au contenu d'une cellule
    :param visible: booléen donnant la visibilité de la cellule
    :return: dictionnaire conforme à une cellule
    """

    # Test si le contenu est conforme puis si la visibilité est bien un booléen
    if isContenuCorrect(content) != True :
        raise ValueError(f"construireCellule : le contenu {content} n'est pas correct")
    if type(visible) != bool :
        raise TypeError(f"onstruireCellule : le contenu {visible} n'est pas un booléen")

    # Renvoi du dictionnaire conforme à une cellule
    return { const.CONTENU : content, const.VISIBLE : visible, const.ANNOTATION : None }


def getContenuCellule(cellule: dict) -> int :
    """
    Cette fonction récupère le contenu d'une cellule

    :param cellule: dictionnaire conforme à une cellule
    :return: entier représentant le contenu de la cellule
    """

    # Test de la conformité du dictionnaire
    if type_cellule(cellule) != True :
        raise TypeError("getContenuCellule : Le paramètre n’est pas une cellule")

    # Renvoi du contenu de la cellule
    return cellule[const.CONTENU]


def isVisibleCellule(cellule : dict) -> bool :
    """
    Cette fonction vérifie si une cellule est visible ou non

    :param cellule: dictionnaire conforme à une cellule
    :return: True si la cellule est visible, False si elle ne l'est pas
    """

    # Test de conformité du dictionnaire
    if type_cellule(cellule) != True :
        raise TypeError("isVisibleCellule : Le paramètre n’est pas une cellule")

    # Renvoi le paramètre de visibilité de la cellule ( True si visible, False si non visible )
    return cellule[const.VISIBLE]


def setContenuCellule(cellule: dict, content: int) -> None:
    """
    Cette fonction permet de modifier le contenu d'une cellule déjà existante

    :param cellule: dictionnaire conforme à une une cellule
    :param content: entier confomre à un contenu de cellule
    :return: None
    """

    # Test de si le contenu est un entier
    if type(content) != int :
        raise TypeError("setContenuCellule : Le second paramètre n’est pas un entier.")
    # Test la conformité du contenu
    if content > 8 or content < 0 and content != const.ID_MINE:
        raise ValueError(f"setContenuCellule : la valeur du contenu {content} n’est pas correcte.")
    # Test la conformité de la cellule
    if type_cellule(cellule) != True :
        raise TypeError("setContenuCellule : Le premier paramètre n’est pas une cellule.")

    # Modification du contenu de la cellule par content
    cellule[const.CONTENU] = content

    return None


def setVisibleCellule(cellule: dict, visible: bool) -> None :
    """
    Cette fonction permet de modifier la visibilité d'une cellule déjà éxistante

    :param cellule: dictionnaire conforme à une cellule
    :param visible: booléen donnant la visibilité de la cellule
    :return: None
    """

    # Test de la conformité de la cellule
    if type_cellule(cellule) != True :
        raise TypeError("setVisibleCellule : Le premier paramètre n’est pas une cellule.")
    # Test si visible est bien un booléen
    if type(visible) != bool :
        raise TypeError("setVisibleCellule : Le second paramètre n’est pas un booléen")

    # Modification de la visibilité de la cellule par visible
    cellule[const.VISIBLE] = visible

    return None

def contientMineCellule(cellule: dict) -> bool :
    """
    Cette fonction permet de vérifier si contient une mine ou non

    :param cellule: dictionnaire conforme à une cellule
    :return: True si la cellule contient une mine, False si la cellule n'en contient pas
    """

    # Test la conformité de la cellule
    if type_cellule(cellule) != True :
        raise TypeError("contientMineCellule : Le paramètre n’est pas une cellule")

    # Renvoi le résultat du test vérifiant si le contenu de la cellule est une mine
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

    :param cellule: dictionnaire conforme à une cellule
    :return: chaîne de carractère stocké comme annotation par la cellule
    """
    # Test si la cellule est conforme
    if type_cellule(cellule) != True :
        raise TypeError("getAnnotationCellule : le paramètre valeur_du paramètre n’est pas une cellule")
    # Test si la cellule ne contiens pas d'annotation, ret vaudra None
    if const.ANNOTATION not in cellule :
        ret = None
    # Sinon ret vaudra l'annotation de la cellule
    else :
        ret = cellule[const.ANNOTATION]

    return ret


def changeAnnotationCellule(cellule: dict) -> None:
    """
    Cette fonction change l'annotation d'une cellule

    :param cellule: dictionnaire conforme à une cellule
    :return: None
    """

    # Test la conformité de la cellule
    if type_cellule(cellule) != True:
        raise TypeError("changeAnnotationCellule : le paramètre n’est pas une cellule")
    # Test si l'annotation de la cellule vaut None, ret vaudra Flag
    if cellule[const.ANNOTATION] == None :
        ret = const.FLAG
    # Sinon si l'annotation vaut FLAG, ret vaudra DOUTE
    elif cellule[const.ANNOTATION] == const.FLAG :
        ret = const.DOUTE
    # Sinon ret vaudra None
    else :
        ret = None

    # Modification de l'annotation de la cellule par ret
    cellule[const.ANNOTATION] = ret

    return None


def reinitialiserCellule(cellule: dict) -> None:
    """
    Cette fonction réinitialise une cellule.

    :param cellule: dictionnaire conforme à une cellule
    :return: None
    """

    # Chaque paramètre de la cellule est remis à son état d'origine
    cellule[const.CONTENU] = 0
    cellule[const.VISIBLE] = False
    cellule[const.ANNOTATION] = None
    
    return None