# tests

LIGNE_6 = [3, 1, 2, 2, 1, 1]
LIGNE_7 = [1, 3, 1, 1, 2, 2, 2, 1]
LIGNE_8 = [1, 1, 1, 3, 2, 1, 3, 2, 1, 1]
assert conway_suivante(LIGNE_6) == LIGNE_7
assert conway_suivante(LIGNE_7) == LIGNE_8


# autres tests
CONWAY = [
    [1],
    [1, 1],
    [2, 1],
    [1, 2, 1, 1],
    [1, 1, 1, 2, 2, 1],
    [3, 1, 2, 2, 1, 1],
    [1, 3, 1, 1, 2, 2, 2, 1],
    [1, 1, 1, 3, 2, 1, 3, 2, 1, 1],
    [3, 1, 1, 3, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1],
    [1, 3, 2, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 1, 1],
    [1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 3, 1, 1, 2, 1, 3, 2, 1, 1, 3, 2, 1, 2, 2, 2, 1],
    [3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 2, 3, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 3, 2, 1, 1],
    [1, 3, 2, 1, 1, 3, 2, 1, 3, 2, 1, 1, 1, 2, 1, 3, 1, 2, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2, 1, 1, 3, 1, 2, 2, 1],
    [1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 1, 3, 1, 2, 3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 2, 1, 3, 2, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 3, 3, 1, 2, 2, 2, 1, 1, 3, 1, 1, 2, 2, 1, 1],
    [3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 3, 1, 1, 1, 2, 1, 3, 2, 1, 1, 2, 3, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 1, 3, 2, 2, 2, 1, 2, 3, 1, 1, 3, 2, 2, 1, 1, 3, 2, 1, 2, 2, 2, 1],
    [1, 3, 2, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 3, 3, 1, 1, 2, 1, 3, 2, 1, 1, 3, 3, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 2, 1, 3, 2, 1, 1, 3, 1, 2, 1, 1, 1, 3, 2, 2, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 3, 3, 2, 1, 1, 1, 2, 1, 3, 2, 1, 1, 3, 2, 2, 2, 1, 1, 3, 1, 2, 1, 1, 3, 2, 1, 1],
    [1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 1, 3, 2, 2, 2, 1, 2, 3, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 2, 3, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 3, 3, 2, 2, 1, 1, 2, 1, 3, 2, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 3, 3, 1, 1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 3, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2, 1, 1, 3, 1, 2, 2, 1],
    [3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 3, 3, 2, 1, 1, 1, 2, 1, 3, 1, 2, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 1, 1, 1, 2, 1, 3, 1, 2, 2, 1, 1, 2, 1, 3, 2, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 3, 3, 1, 1, 2, 1, 3, 2, 1, 2, 3, 2, 2, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 1, 3, 2, 2, 2, 1, 2, 3, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 1, 1, 1, 2, 1, 3, 1, 1, 1, 2, 1, 3, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 2, 3, 2, 2, 2, 1, 1, 3, 3, 1, 2, 2, 2, 1, 1, 3, 1, 1, 2, 2, 1, 1],
    [1, 3, 2, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 3, 3, 1, 1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 2, 1, 3, 2, 1, 1, 3, 2, 1, 2, 2, 3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 1, 3, 2, 2, 2, 1, 1, 2, 1, 3, 2, 1, 1, 3, 2, 1, 3, 2, 2, 1, 2, 3, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 1, 1, 1, 2, 1, 3, 3, 2, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 3, 3, 2, 1, 1, 1, 2, 1, 3, 1, 2, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 2, 1, 1, 1, 3, 3, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 2, 1, 3, 2, 1, 1, 3, 2, 1, 3, 2, 1, 1, 1, 2, 1, 3, 3, 2, 2, 1, 2, 3, 1, 1, 3, 2, 2, 1, 1, 3, 2, 1, 2, 2, 2, 1],
    [1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 1, 3, 2, 2, 2, 1, 2, 3, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 1, 1, 1, 2, 1, 3, 1, 1, 1, 2, 1, 3, 2, 1, 1, 2, 3, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 2, 2, 1, 3, 2, 1, 1, 2, 3, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 3, 3, 2, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 1, 3, 2, 2, 1, 1, 1, 2, 1, 3, 1, 2, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 1, 2, 3, 1, 1, 2, 1, 1, 2, 3, 2, 2, 2, 1, 1, 2, 1, 3, 2, 1, 1, 3, 2, 1, 3, 2, 2, 1, 1, 3, 3, 1, 1, 2, 1, 3, 2, 1, 2, 3, 1, 2, 3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 2, 1, 3, 2, 1, 1, 3, 3, 1, 1, 2, 1, 3, 2, 1, 1, 2, 3, 1, 2, 3, 2, 1, 1, 2, 3, 1, 1, 3, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 3, 1, 2, 2, 1, 1, 3, 1, 2, 1, 1, 1, 3, 1, 2, 3, 1, 1, 2, 1, 1, 2, 3, 2, 2, 1, 1, 1, 2, 1, 3, 2, 1, 1, 3, 2, 2, 2, 1, 1, 3, 1, 2, 1, 1, 3, 2, 1, 1],
]

secret = all(conway_suivante(CONWAY[i-1]) == CONWAY[i]
                for i in range(1, len(CONWAY)))
assert secret, "Erreur à un test secret"
