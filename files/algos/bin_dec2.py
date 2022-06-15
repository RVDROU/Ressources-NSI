def conversion_decimal(nombre_bin):
    """
    convertit un nombre binaire en nombre décimal
    param:
        nombre_bin:str
    return:int
    -------------
    >>> conversion_decimal('1101')
    13
    >>> conversion_decimal('1')
    1
    >>> conversion_decimal('11')
    3
    """
    decimal=0
    for i in range(len(nombre_bin)):
        decimal+=int(nombre_bin[i])*2**(len(nombre_bin)-1-i)
    return decimal
