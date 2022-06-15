def recherche_dicho(val, table):
    '''
    recherche la position de la valeur  dans la table
    
    param :
        table : list : liste ordonnée de valeurs
        val : type identique aux éléments de la liste
    
    return : 
        int : position de la valeur dans table
        False : si valeur n'est pas dans table
    
    Exemple :
    >>> recherche_dicho(14, [10, 11, 11, 12, 13, 15, 18, 23, 41])
    >>> recherche_dicho(23, [10, 11, 11, 12, 13, 15, 18, 23, 41])
    7
    
    '''
    d = 0
    f = len(table)-1
    while d<=f:
        m = (d+f) // 2
        if table[m] == val :
            return m
        elif val > table[m]:
            d = m+1
        else:
            f = m -1
    return False
