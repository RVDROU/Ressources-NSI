def maximum(nombres):
    maxi = 0
    for nb in nombres:
        if nb > maxi:
            maxi = nb
    return maxi


def tri_denombrement(nombres):
    maxi = maximum(nombres)

    effectifs = [0] * (maxi + 1)

    for nb in nombres:
        effectifs[nb] += 1

    nombres_tries = []
    for n in range(maxi + 1):
        for i in range(effectifs[n]):
            nombres_tries.append(n)

    return nombres_tries


# Tests
liste = [4, 5, 4, 2]
assert tri_denombrement(liste) == [2, 4, 4, 5]
liste = [3, 8, 7, 3, 5]
assert tri_denombrement(liste) == [3, 3, 5, 7, 8]
liste = [1, 2, 3, 4, 5]
assert tri_denombrement(liste) == [1, 2, 3, 4, 5]
liste = [5, 4, 3, 2, 1]
assert tri_denombrement(liste) == [1, 2, 3, 4, 5]
liste = []
assert tri_denombrement(liste) == []

# Tests supplémentaires
liste = [4, 4, 4]
assert tri_denombrement(liste) == [4, 4, 4]
liste = [k for k in range(100, -1, -1)]
assert tri_denombrement(liste) == list(range(101))
liste = [1, 2]*10
assert tri_denombrement(liste) == [1]*10+[2]*10
liste = [10**3, 0]
assert tri_denombrement(liste) == [0, 10**3]
