# tests

assert delannoy(3, 3) == 63
assert delannoy(2, 1) == 5


# autres tests

DELANNOY = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 3, 5, 7, 9, 11, 13, 15, 17],
    [1, 5, 13, 25, 41, 61, 85, 113, 145],
    [1, 7, 25, 63, 129, 231, 377, 575, 833],
    [1, 9, 41, 129, 321, 681, 1289, 2241, 3649],
    [1, 11, 61, 231, 681, 1683, 3653, 7183, 13073],
    [1, 13, 85, 377, 1289, 3653, 8989, 19825, 40081],
    [1, 15, 113, 575, 2241, 7183, 19825, 48639, 108545],
    [1, 17, 145, 833, 3649, 13073, 40081, 108545, 265729],
]

for n in range(9):
    for m in range(9):
        attendu = DELANNOY[n][m]
        assert delannoy(n, m) == attendu, f"Erreur avec n = {n} et m = {m}."

