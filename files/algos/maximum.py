def maximum(liste):
    if liste != []:
        maximum = liste[0]
        for i in range(len(liste)):
            if liste[i] > maximum:
                maximum = liste[i]
        return maximum
