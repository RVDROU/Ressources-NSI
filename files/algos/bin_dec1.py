def conv_bin_dec(binaire):
    '''
    convertit un nombre binaire en un nombre décimal
    
    :param :
    --------
    binaire : str   nombre bianire à convertir
    
    :return:
    --------
    int : valeur en base 10

    :Exemples:
    ----------
    >>> conv_bin_dec("0010")
    2
    >>> conv_bin_dec("101010110")
    342
    >>> conv_bin_dec('0')
    0
    
    '''
    decimal=0
    for bit in binaire:
        decimal = decimal*2 + int(bit)
    return decimal
