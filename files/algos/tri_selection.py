def index_min(donnees, indice):
    """retourne l'indice du plus petit élément d'une liste, à partir d'un indice donné

    Exemple:
    
    >>> index_min(["curl", "bash", "python", "cilk", "nesl"], 0)
    1
    >>> index_min(["curl", "bash", "python", "cilk", "nesl"], 2)
    3
    
    """
    pos = indice
    for i in range(indice, len(donnees)):
        if donnees[i]<donnees[pos] :
            pos = i
    return pos

def tri_selection(donnees):
    """tri la liste donnees en place, avec l'algorithme de tri par sélection

    >>> liste3 = [ "ruby", "python", "logo", "elan", "rust"]
    >>> tri_selection(liste3)
    >>> liste3
    ['elan', 'logo', 'python', 'ruby', 'rust']
    
    """
    for i in range(len(donnees)-1):
        j = index_min(donnees,i)
        donnees[i], donnees[j] = donnees[j], donnees[i]
