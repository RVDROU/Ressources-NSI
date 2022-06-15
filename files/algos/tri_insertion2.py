def insere2(liste, valeur):
    """Insère la valeur dans la liste, supposée triée. la modification est en place

    param :
        liste : list : liste de nombres
        valeur : float/int
    return :
        list : nouvelle liste avec la valeur insérée

    Exemple:
    >>> liste1 = [3,5.2,6]
    >>> insere2(liste1, 4)
    >>> liste1
    [3, 4, 5.2, 6]
    """
    liste.append(valeur)
    indice = len(liste)-1
    while indice>0 and liste[indice-1] > liste[indice]:
        liste[indice],liste[indice-1] = liste[indice-1],liste[indice]
        indice = indice - 1
    

def tri_insertion2(liste):
    """renvoie une nouvelle liste qui est une version triée de liste

    param :
        liste : list
    return :
        liste

    Exemple :
    >>> tri_insertion2([8,2,6,5])
    [2, 5, 6, 8]
    """
    liste_triee = []
    for element in liste:
        insere2(liste_triee, element)
    return liste_triee
