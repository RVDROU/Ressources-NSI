def conv_dec_bin(entier):
    """ cette fonction permet de convertir un nombre entier en binaire

    param
    -----
    entier : int
    
    return
    ------
    str : chaine de caractères composée de 0 et de 1 
    
    exemples:
    ---------
    >>> conv_dec_bin(13)
    '1101'
    
    >>> conv_dec_bin(192)
    '11000000'
    
    """
    reponse = ""
    if entier == 0:
        return "0"
    else:
        while entier !=0:
            reste = entier%2
            reponse = str(reste) + reponse 
            entier = entier//2
    return reponse
