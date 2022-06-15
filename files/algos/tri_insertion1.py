def insere(donnees, indice):
    """insere la donnee d'indice i à sa bonne place dans la liste formée des
    éléments d'indice inférieur ou égaux à i.
    Le début de la liste est sensé être trié.
    LA MODIFICATION SE FAIT EN PLACE
    
    param :
        donnees : list
        indice : int
        
    exemple :
    >>> a = [3, 9, 5, 6, 4, 1]
    >>> insere(a, 2)
    >>> a
    [3, 5, 9, 6, 4, 1]
    
    """
    while indice>0 and donnees[indice]<donnees[indice-1]:
        donnees[indice-1], donnees[indice] = donnees[indice], donnees[indice-1]
        indice = indice -1

def tri_insertion(donnees):
    """tri la liste donnees en place, avec l'algorithme de tri par insertion
    LE TRI SE FAIT EN PLACE.
    
    param :
        donnees : list
        
    exemple :
    >>> liste3 = [ "ruby", "python", "logo", "elan", "rust"]
    >>> tri_insertion(liste3)
    >>> liste3
    ['elan', 'logo', 'python', 'ruby', 'rust']
    
    """
    for ind in range(len(donnees)):
        insere(donnees,ind)
