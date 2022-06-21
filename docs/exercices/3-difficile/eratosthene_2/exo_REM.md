# Commentaires

## Force brute

```python
def est_premier(n):
    if n < 2:
        return False
    for d in range(2, n):
        # 1 < d < n
        if n % d == 0:
            # d est un diviseur de n, autre que 1 et n
            return False
    return True

def crible_brute(limite):
    return [est_premier(i) for i in range(limite)]
```

Il s'agit d'une traduction directe de la définition.

Cette version est lente, en effet le cout du calcul pour `est_premier(n)` est dans le pire des cas de `n` tours de boucles. La somme des couts pour `i` allant de zéro jusqu'à la limite est importante.

## Première version du crible

```python
def eratosthene(n):
    crible = [True] * n
    if n > 0:
        crible[0] = False  # 0 n'est pas premier
    if n > 1:
        crible[1] = False  # 1 n'est pas premier
    for p in range(2, n):
        if crible[p]:
            # p est premier
            for kp in range(2*p, n, p):
                # kp est un multiple de p, donc non premier
                crible[kp] = False
    return crible
```

## Deuxième version

```python
def eratosthene_V2(n):
    crible = [True] * n
    if n > 0:
        crible[0] = False  # 0 n'est pas premier
    if n > 1:
        crible[1] = False  # 1 n'est pas premier
    p = 2
    while p * p < n:
        if crible[p]:
            # p est premier
            for kp in range(p*p, n, p):
                # kp est un multiple de p, donc non premier
                crible[kp] = False
        p += 1
    return crible
```

La principale différence est que la boucle interne commence à $p^2$, en effet les multiples précédents de $p$ ont déjà été marqués comme composés.

On a alors remplacé la boucle externe par une boucle `while` qui s'arrête quand $p^2$ atteint la limite $n$.

## Troisième version

Voici quelques astuces pour améliorer le crible.


```python
def eratosthene_V3(n):
    crible = bytearray([True]) * n
    if n > 0:
        crible[0] = False  # 0 n'est pas premier
    if n > 1:
        crible[1] = False  # 1 n'est pas premier
    p = 2
    while p * p < n:
        if crible[p]:
            crible[p*p:n:p] = bytearray([False]) * len(crible[p*p:n:p])
        p += 1
    return crible
```

1. Un booléen prend beaucoup de place en Python pour la quantité d'information qu'il porte. Une liste de booléen accentue fortement cet effet. On utilise alors `byterray` qui fonctionne exactement comme une liste, mais ses éléments sont des entiers sur un octet seulement, au lieu de plusieurs pour les listes. Il y a un gain important en mémoire, donc en temps !
2. On remplace la boucle interne par une affectation d'une tranche par une autre tranche.

Il reste une autre bonne amélioration à mettre en place.

On peut calculer `#!py len(crible[p*p:n:p])` en fonction de `n` et de `p` ; ce qui évite un parcours de cette tranche. C'est à vous de trouver la formule !

Pour rechercher encore l'optimisation, mais au prix d'un code plus lourd, on pourra créer une liste ne modélisant que les nombres impairs. On fera le crible directement sur cette liste qui prend deux fois moins de place.

:warning: On pensera lors de la génération des nombres premiers à ajouter 2 au début.

Cette optimisation fera l'objet d'un exercice...
