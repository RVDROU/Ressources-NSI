def nombre_occurrences(chaine, carac):
    '''Renvoie le nombre d'occurrences de carac dans chaine

    param : 
        chaine : str
        carac : str
    return :
        int
    
    exemple :
    >>> nombre_occurences("bonjour","o")
    2
    >>> nombre_occurences("bonjour","z")
    0
    '''
    compteur = 0
    for car in chaine:
        if car == carac:
            compteur = compteur +1
    return compteur
