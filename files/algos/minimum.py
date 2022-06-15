def minimum(liste):
    if liste != []:
        minimum = liste[0]
        for element in liste:
            if element < minimum:
                minimum = element
        return minimum
