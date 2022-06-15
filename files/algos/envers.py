def renverse(chaine):
    """Renvoie la chaîne de caractère renversée, le dernier caractère devient le premier, l'avant dernier
    le deuxième et ainsi de suite...

    param : 
        chaine : str
    return :
        str
    
    exemple :
    >>> renverse("Bonjour")
    'ruojnoB'

    >>> renverse("")
    ''
    """
    renverse = ""
    for caractere in chaine:
        renverse = caractere + renverse
    return renverse
