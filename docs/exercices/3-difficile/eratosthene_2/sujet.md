---
author: Franck Chambon
title: Crible d'Ératosthène V2
search:
    - exclude: True
---
**Objectif** : obtenir la primalité des nombres de $2$ jusqu'à $n$.

!!! info "Nombres premiers"
    **Définition** : Un nombre $p$ est premier si c'est un entier supérieur ou égal à $2$ qui n'a que deux diviseurs : $1$ et lui-même.

    D'après la définition, on peut écrire directement

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
    ```

    On peut déduire la liste des nombres premiers inférieurs à $20$.

    ```pycon
    >>> [n for n in range(20) if est_premier(n)]
    [2, 3, 5, 7, 11, 13, 17, 19]
    ```

    **Cette méthode est lente.**


**Améliorations du crible classique**

On peut rassembler la primalité des nombres inférieurs à $20$ dans un tableau de booléens :

```pycon
>>> # indice        0      1     2     3      4     5      6     7      8     9      10    11     12     13      14    15      16    17     18    19
>>> primalite = [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]
>>> primalite[5]
True
>>> primalite[6]
False
```

Objectif : Construire rapidement un tel tableau.

Méthode : On peut utiliser le crible d'Ératosthène. Il existe plusieurs variantes, voici une version intermédiaire. Vous avez déjà rencontré une première version qui ressemble à :

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

On peut vérifier ceci avec les tests

```pycon
>>> limite = 20
>>> primalite = eratosthene(limite)
>>> primalite_brute = [est_premier(i) for i in range(limite)]
>>> primalite == primalite_brute
True
```


L'objectif de l'exercice est d'améliorer la fonction `eratosthene` en suivant les conseils suivants :

1. Remplacer la ligne `#!py for p in range(2, n):` par une structure avec une boucle `while`.
2. Remplacer la ligne `#!py for kp in range(2*p, n, p):` par `#!py for kp in range(p*p, n, p):`, en effet les multiples de $2p$ inclus à $p^2$ exclu ont déjà été cochés.
3. En déduire que quand $p×p >= n$ il n'y plus de nouveaux multiples à cocher. Ils ont tous déjà été cochés. C'est une propriété mathématique : « Si un entier $n$ est composé, alors il possède un diviseur premier inférieur ou égal à $\sqrt{n}$ ».
4. Modifier la boucle `while` en conséquence.
5. Tester votre fonction `eratosthene_V2` en la confrontant à `eratosthene` et à une méthode par force brute.

**Génération des nombres premiers**

Quand vous aurez terminé, vous pourrez tester une astuce avec Python pour générer la liste des nombres premiers à partir du tableau de booléens `primalite`.

Lire [la documentation](https://docs.python.org/fr/3/library/itertools.html#itertools.compress) au sujet de `itertools.compress`

```pycon
>>> from itertools import compress
>>> limite = 20
>>> primalite = eratosthene(limite)
>>> list(compress(range(limite), primalite))
[2, 3, 5, 7, 11, 13, 17 ,19]
```

Pour tester cela, construire une fonction telle que `somme_premiers(n)` renvoie la somme des nombres premiers strictement inférieurs à $n$.

!!! example "Exemples"

    ```pycon
    >>> somme_premiers(5)
    5
    >>> somme_premiers(20)
    77
    ```

{{ IDE('exo') }}

> Vous ajouterez tous les tests utiles aux différentes étapes.
