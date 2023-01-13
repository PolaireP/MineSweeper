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
    :return: liste conforme à une grille de démineur
    """

    # Test si le nombre de ligne et le nombre de colonne sont inférieur
    # ou égal à 0
    if nb_ligne <= 0 or nb_col <= 0 :
        raise ValueError(f"onstruireGrilleDemineur : Le nombre de lignes {nb_ligne} ou de colonnes {nb_col} est négatif ou nul")
    # Test si le nombre de colonnes et le nombre de ligne
    # sont bien des entiers
    if type(nb_col) != int or type(nb_ligne) != int :
        raise TypeError(f" construireGrilleDemineur : Le nombre de lignes {nb_ligne} ou de colonnes {nb_col} n’est pas un entier.")

    # Création de la grille vide
    grille = []

    # Remplissage de la grille avec un nombre de ligne nb_ligne
    # Puis remplissage des lignes avec un nombre de cellule vides nb_col
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
    # Test si la grille n'est pas une grille de démineur
    if type_grille_demineur(grille) != True:
        raise TypeError(f"getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")

    # Renvoi de la taille de la grille ( nombre de lignes )
    return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction récupère le nombre de ligne d'une grille de démineur.

    :param grille: liste conforme à une grille de démineur
    :return: entier représentant le nombre de colonnes d'une grille
    """
    # Test si la grille n'est pas une grille de démineur
    if type_grille_demineur(grille) != True:
        raise TypeError("getNbColonnesGrilleDemineur : Le paramètre n’est pas une grille")

    # Renvoi la taille de la première ligne de la ligne ( nombre de colonnes )
    return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    """
    Vérifie si une coordonnée est présente dans une grille

    :param grille: liste conforme à une grille de démineur
    :param coord: tuple représentant une coordonée dans la grille
    :return: True si la coordonnée est dans la grille, False si elle ne l'est pas
    """

    # Vérifie si une grille est bien une grille de démineur
    # et si la coordonnée est bien un tuple
    if type_grille_demineur(grille) != True or type(coord) != tuple:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")

    # Initialisation de estCoord
    estCoord = True

    # Vérifie si la première valeur de coord n'est pas inférieur au nombre de ligne
    # ou si la seconde valeur n'est pas inférieur au nombre de ligne
    # ou bien si l'une des deux valeurs est négative
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
    # Test que la grille et la coordonné soient bien une grille de démineur et une coordonnée
    if type_grille_demineur(grille) != True or type_coordonnee(coord) != True:
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    # Vérifie que la coordonnée est bien dans la grille
    if isCoordonneeCorrecte(grille, coord) != True:
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille")

    # Renvoie la cellule à la coordonnée de la grille
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
    :return: None
    """
    # Vérifie si la coordonnée est dans la grille
    isCoordonneeCorrecte(grille, coord)
    # Test si le contenu est correct
    isContenuCorrect(content)

    # Change le contenu de la cellule pour mettre le nouveau contenu
    setContenuCellule(grille[coord[0]][coord[1]], content)

    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Cette fonction renvoi le paramètre de visibilité d'une cellule d'une grille

    :param grille: liste conforme à une liste de démineur
    :param coord: tuple conforme à une coordonnée
    :return: True si la cellule est visible, sinon False
    """

    # Vérifie si la coordonnée est dans la grille
    isCoordonneeCorrecte(grille, coord)

    return grille[coord[0]][coord[1]][const.VISIBLE]


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    """
    Cette fonction change le paramètre de visibilité d'une cellule de la grille

    :param grille: liste conforme à une liste de démineur
    :param coord: tuple conforme à une coordonnée
    :param visible: bool représentant la nouvelle visibilité de la cellule
    :return: None
    """
    # Vérifie si la coordonnée est dans la grille
    isCoordonneeCorrecte(grille, coord)
    # Change le paramètre de visibilité pour le nouveau
    setVisibleCellule(grille[coord[0]][coord[1]], visible)

    return None


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    """
    Cette fonction vérifie si la cellule de la grille est une Mine ou non

    :param grille: liste conforme à une liste de démineur
    :param coord: tuple conforme à une coordonnée
    :return: True si la cellule contient une mine, sinon False
    """
    # Vérifie si la coordonnée est dans la grille
    isCoordonneeCorrecte(grille, coord)

    return contientMineCellule(grille[coord[0]][coord[1]])


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    """
    Cette fonction récupère les coordonnées des celulles voisines d'une cellule donnée

    :param grille: liste conforme à une liste de démineur
    :param coord: tuple conforme à une coordonnée
    :return: liste des coordonées des cellules voisines
    """
    # Vérifie que la grille et la coordonée sont de bon type
    if type_grille_demineur(grille) != True or type(coord) != tuple :
        raise TypeError("getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    # Vérifie si la coordonnée est dans la grille
    if isCoordonneeCorrecte(grille, coord) == False :
        raise IndexError("getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")

    # Initialisation de la position horizontale
    h = coord[0]
    # Initialisation de la position verticale
    v = coord[1]
    # Initialisation de la liste des voisins
    voisins = []

    # Pour chaque case autour de la cellule
    for i in range(h-1, h+2):
        for j in range(v-1, v+2):
            # Tester si la coordonnée est correcte
            # Si oui, ajouter la coordonnée à voisins
            if isCoordonneeCorrecte(grille, (i, j)) and (i, j) != coord:
                voisins.append((i, j))
    return voisins


def placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple) -> None:
    """
    Cette fonction place les mines sur la grille

    :param grille: liste conforme à une grille du démineur
    :param nb: entier représentant le nombre de mines à placer
    :param coord: tuple conforme à une coordonnée
    :return: None
    """

    # Teste que le nombre de mine à placer soit positif
    # et inférieur au nombre de cellule
    if nb < 0 or nb >= getNbColonnesGrilleDemineur(grille) * getNbLignesGrilleDemineur(grille) :
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorect")
    # Vérifie que la coordonnée soit bien dans la grille
    if isCoordonneeCorrecte(grille, coord) == False :
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille")

    # Initialisation du nombre de ligne
    lignes = getNbLignesGrilleDemineur(grille)
    # Initialisation du nombre de colonnes
    cols = getNbColonnesGrilleDemineur(grille)

    # Calcul nb coordonnées aléatoire rentrant dans la grille
    # en évitant la case cliquée.
    for i in range(nb):
        x = randint(0, lignes - 1)
        y = randint(0, cols - 1)
        # Tant que la coordonnée calculée correspon à coord
        # ou que c'est une mine déjà placée, on relance le calcul
        while getContenuCellule(grille[x][y]) == const.ID_MINE or (x == coord[0] and y == coord[1]) :
            x = randint(0, lignes - 1)
            y = randint(0, cols - 1)

        # Changement du contenu de la cellule en mine
        setContenuCellule(grille[x][y], const.ID_MINE)
    # Comptage des mines autour des cellules
    compterMinesVoisinesGrilleDemineur(grille)

    return None


def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    """
    Cette fonction ajoute pour chaque cellule le nombre de mine autour

    :param grille: liste coonforme à une grille de démineur
    :return: None
    """

    # Pour chaque cellule
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):

            # Si son contenu n'est pas une mine
            if getContenuCellule(grille[i][j]) != const.ID_MINE:
                voisins = getCoordonneeVoisinsGrilleDemineur(grille, (i, j))
                # Lancer le calcul des mines autour
                for k in range(len(voisins)):
                    cell = voisins[k]
                    # Si le contenu du voisin est une mine
                    # ajouter +1 au contenu de la cellule de départ
                    if getContenuCellule(grille[cell[0]][cell[1]]) == const.ID_MINE:
                        setContenuCellule(grille[i][j], getContenuCellule(grille[i][j])+1)
    return None


def getNbMinesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction renvoie le nombre de mines contenues dans la liste

    :param grille: liste conforme à une grille de démineur
    :return: nombre entier de mines dans la grille
    """

    # Vérifie que la grille est bien une grille conforme
    if type_grille_demineur(grille) != True:
        raise ValueError("getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")

    # Initialisation du compteur
    compte = 0
    # Test le contenu de chaque cellule de la grille
    for ligne in grille:
        for cellule in ligne :
            # Si la cellule contient une mine, augmentation
            # du compteur de +1
            if cellule[const.CONTENU] == const.ID_MINE:
                compte += 1
    return compte


def getAnnotationGrilleDemineur(grille: list, coord: tuple) -> str:
    """
    Cette fonction récupère l'annotation d'une cellule de la grille.

    :param grille: liste conforme à une grille de démineur
    :param coord: tuple conforme à une coordonnées de cellule
    :return: Str représentant l'annotation de la cellule
    """
    return getAnnotationCellule(grille[coord[0]][coord[1]])


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """
    Cette fonction compte le nombre de mines à marquer

    :param grille: liste conforme à une grille de démineur
    :return: entier représentant le nombre de mine à marquer
    """

    # Initialisation du compteur
    compte = 0

    # Pour chaque cellule
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):

            # Si la cellule a un drapeau ajouter 1 au compteur
            if getAnnotationGrilleDemineur(grille, (i, j)) == const.FLAG :
                compte += 1
    # Renvoi nombre total de mines moins compteur
    return getNbMinesGrilleDemineur(grille) - compte


def gagneGrilleDemineur(grille: list) -> bool:
    """
    La fonction vérifie si la partie est gagnée ou non

    :param grille: liste conforme à une grille de démineur
    :return: True si la partie est gagnée, False sinon
    """
    # Initialisation de gagner
    gagner = True

    # Pour chaque cellule lancer des tests
    # passant gagner à False si au moins un renvoie True
    for ligne in grille :
        for case in ligne :
            # Si la cellule n'est pas une mine et n'est pas visible
            if getContenuCellule(case) != const.ID_MINE and isVisibleCellule(case) != True :
                gagner = False
            # Sinon si la cellule est une mine visible
            elif getContenuCellule(case) == const.ID_MINE and isVisibleCellule(case) == True :
                gagner = False
            # Sinon si la cellule est une mine non visible et pas marqué d'un drapeau
            elif getContenuCellule(case) == const.ID_MINE and isVisibleCellule(case) == False and getAnnotationCellule(case) != const.FLAG :
                gagner = False
    return gagner


def perduGrilleDemineur(grille: list) -> bool:
    """
    Cette fonction vérifie si une partie est perdue

    :param grille: liste conforme à une grille de démineur
    :return: True si la partie est perdue, False sinon
    """

    # Initialisation de perdu
    perdu = False

    # Pour chaque cellule
    for ligne in grille :
        for case in ligne :
            # Si la cellule est une mine visible passer perdu à True
            if getContenuCellule(case) == const.ID_MINE and isVisibleCellule(case) == True :
                perdu = True
    return perdu


def reinitialiserGrilleDemineur(grille: list) -> None:
    """
    Cette fonction réinitialise toutes les cellules d'une grille de démineur

    :param grille: liste conforme à une grille de démineur
    :return: None
    """

    # Pour chaque cellule
    for ligne in grille :
        for case in ligne :
            reinitialiserCellule(case)

    return None


def decouvrirGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Cette fonction découvre une cellule à la position coord d'une
    grille et découvre son voisinage automatiquement si la cellule
    n'as pas de mine autour.

    :param grille: liste conforme à une grille de démineur
    :param coord: tuple conforme à une coordonnée
    :return: None
    """

    # Initialisation de l'ensemble vue et de la liste aVoir
    vue = set()
    aVoir = [coord]

    # Tant que aVoir n'est pas vide
    while len(aVoir) != 0:
        # Initialisation de cellule dans aVoir
        cellule = aVoir[0]

        # Si cellule n'est pas dans vue :
        if cellule not in vue :
            # La rendre visible
            setVisibleGrilleDemineur(grille, cellule, True)
            # Si la cellule n'a aucune mine autour ajouter son voisinage
            # à aVoir
            if getContenuGrilleDemineur(grille, cellule) == 0 :
                aVoir += getCoordonneeVoisinsGrilleDemineur(grille, cellule)
            # Ajout de la cellule dans l'ensemble vue
            vue.add(cellule)
        # Supression de la cellule dans la liste aVoir
        aVoir.remove(cellule)

    return vue


def simplifierGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Cette fonction permet de rendre visible les cases voisines si
    le nombre de cases voisine doté d'un drapeau est le même que
    celui dans le contenu de la case.

    :param grille: liste conforme à une grille de démineur
    :param coord: tuple conforme à une coordonnée
    :return: ensemble de coordonnées des cases à rendre visible
    """
    # Initialisation de l'ensemble des coordonnées découvertes
    # ainsi que des cellules à vérifier
    coordonnees_decouvertes = set()
    cellulesVerif = [coord]

    # Tant qu'il reste des cellules à vérifier
    while len(cellulesVerif) > 0:
        # Sortir une cellule et la mettre dans cellule_courante
        cellule_courante = cellulesVerif.pop()
        #  vérifie que la visibilité de la cellule
        if isVisibleGrilleDemineur(grille, cellule_courante):
            coordonnees_decouvertes.add(cellule_courante)
            # Initialisation du compteur et du voisinage
            nb_drapeaux_voisinage = 0
            voisinage = getCoordonneeVoisinsGrilleDemineur(grille, cellule_courante)
            # Comptage des cellules doté d'un drapeau dans le voisinage, ces cellules
            # sont enlevées de la liste voisinage
            for i in range(len(voisinage)-1, -1, -1):
                if getAnnotationGrilleDemineur(grille, voisinage[i]) == const.FLAG:
                    nb_drapeaux_voisinage += 1
                    voisinage.pop(i)

            # Si ce nombre correspond exactement au contenu de la cellule, la fonction
            # rend toutes les autres cases voisines visibles et les ajoute dans les cellules à vérifier.
            if getContenuGrilleDemineur(grille, cellule_courante) == nb_drapeaux_voisinage:
                for voisin in voisinage:
                    if voisin not in cellulesVerif and voisin not in coordonnees_decouvertes:
                        setVisibleGrilleDemineur(grille, voisin, True)
                        cellulesVerif.append(voisin)

    return coordonnees_decouvertes


def ajouterFlagsGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Ajoute un drapeau si son plaçage est évident

    :param grille: liste conforme à une grille de démineur
    :param coord: ruple conforme à une coordonnée
    :return: ensemble des coordonnées à changer
    """
    # Initialisation des valeurs
    ensemble = set()
    contenu = getContenuGrilleDemineur(grille, coord)
    compte = 0
    tempo = []
    # Pour chaque voisin l'ajouter à une liste temporaire si il n'est pas visible
    # Et augmenter le compteur de 1
    for voisin in getCoordonneeVoisinsGrilleDemineur(grille, coord):
        if isVisibleGrilleDemineur(grille, voisin) != True :
            compte += 1
            tempo.append(voisin)
    # Si le compteur est égal au nombre contenu dans la case
    # Alors on ajoute les cases stockées à notre ensemble
    if compte == contenu :
        for case in tempo :
            while getAnnotationCellule(grille[case[0]][case[1]]) != const.FLAG:
                changeAnnotationCellule(grille[case[0]][case[1]])
            ensemble.add(case)
    return ensemble


def simplifierToutGrilleDemineur(grille: list) -> tuple:
    """
    Cette fonction résoud la grille du démineur

    :param grille: liste conforme à une grille de démineur
    :return: ensemble des cases visibles et marqué d'un drapeau
    """

    # Initialisation des ensembles stockant les cases visibles et les Flags et de la variable decouvre
    totalFlag = set()
    totalVisible = set()
    decouvre = True

    # Tant que on a pas gagné ou que totalFlag et totalVisible ne valent pas pareil qu'au tour d'avant
    while gagneGrilleDemineur(grille) == False and decouvre == True:
        # Création des copies des ensembles
        copieVisible = totalVisible.copy()
        copieFlag = totalFlag.copy()

        # Pour k de 1 à 0 compris
        for k in range(1, -1, -1):
            # Se déplacer dans chaque ligne de la grille
            for i in range(getNbLignesGrilleDemineur(grille)):
                # En fonction des lignes et de l'avancement de k, prendre une cellule sur deux
                # l'avancement de k inversera la cellule prise au 2eme passage
                for j in range((i%2)+k, getNbColonnesGrilleDemineur(grille), 2):

                    # Si la cellule est visible et qu'elle n'a pas de drapeau
                    if isVisibleGrilleDemineur(grille, construireCoordonnee(i, j)) and getAnnotationGrilleDemineur(grille, construireCoordonnee(i, j)) != const.FLAG :

                        # Initialiser le voisinage et un compteur
                        voisinage = getCoordonneeVoisinsGrilleDemineur(grille, (i, j))
                        ct = 0

                        # Compteur pour la vérification permettant de passer les cellules dont les voisins sont soit déjà visible
                        # soit avec des drapeaux.
                        for voisin in voisinage :
                            if isVisibleGrilleDemineur(grille, voisin) or getAnnotationGrilleDemineur(grille, voisin) == const.FLAG :
                                ct += 1
                        # Si la cellule a au moins un voisin non visible sans drapeau, lancer la simplification et l'ajout
                        # de drapeaux.
                        if ct != len(voisinage):
                            totalVisible.update(simplifierGrilleDemineur(grille, (i, j)))
                            totalFlag.update(ajouterFlagsGrilleDemineur(grille, (i, j)))
        # Si les ensemble n'ont pas changé depuis la dernière boucle ( cas où la simplification totale est impossible )
        # alors la condition decouvre passe à False et arr^ète la boucle while
        if totalVisible == copieVisible and totalFlag == copieFlag :
            decouvre = False


    return(totalVisible, totalFlag)
