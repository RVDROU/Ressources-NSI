def insere3(liste, valeur):
    """Insère la valeur dans la liste, supposée triée

    param :
        liste : list : liste de nombres
        valeur : float/int
    return :
        list : nouvelle liste avec la valeur insérée

    Exemple:
    >>> liste1 = [3,5.2,6]
    >>> liste2 = insere3(liste1, 4)
    >>> liste2
    [3, 4, 5.2, 6]
    """
    if liste == []:
        return [valeur]
    elif liste[-1]>valeur:
        return insere3(liste[:-1],valeur) + [liste[-1]]
    else:
        return liste + [valeur]

def tri_recursif_insertion3(liste):
    """renvoie une nouvelle liste qui est une version triée de liste. Méthode récursive.

    param :
        liste : list
    return :
        liste

    Exemple :
    >>> tri_recursif_insertion3([8,2,6,5])
    [2, 5, 6, 8]
    """
    if liste == []:
        return []
    else:
        return insere3(tri_recursif_insertion3(liste[:-1]),liste[-1])
