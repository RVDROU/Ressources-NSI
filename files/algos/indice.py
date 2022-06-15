def indice(car, string):
    """Renvoie l'indice de la première occurrence du caractère car dans la chaine string. Renvoie -1 si car n'est pas dans string.

    param :
        string : str
        car : str
    return :
        int

    exemple : 
    >>> indice("o", "Bonjour")
    1
    >>> indice("", "Bonjour")
    -1
    >>> indice("b", "Bonjour")
    -1
    """
    
    indice = 0
    while indice < len(string):
        if string[indice] == car:
            return indice
        indice = indice + 1
    return -1
