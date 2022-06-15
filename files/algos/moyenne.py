def moyenne(liste):
    """renvoie la valeur moyenne d'une liste de nombres et None en cas de liste vide.

    param:
        liste : list
    return :
        float

    exemple :

    >>> moyenne([1,2,4])
    3.5
    >>> moyenne([])

    """
    if liste != []:
        somme = 0
        for elt in liste:
            somme = somme +elt
        return somme/len(liste)
