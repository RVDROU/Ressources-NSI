

### Suite de Syracuse 


Pour construire la suite de Syracuse d'un entier $n$ :

- On crée une liste avec $n$ comme premier élément,
- On répète en boucle tant que $n \neq 1$ :
    - Si $n$ est pair, on le divise par $2$,
    - Sinon $n$ devient $3n+1$.
    - On ajoute $n$ à la liste.

On admet que, quel que soit l'entier $n$ choisi au départ, la suite finit toujours par atteindre la valeur $1$.

Écrire une fonction `syracuse` prenant en paramètres un entier `n` strictement positif et qui renvoie la suite de Syracuse de l'entier `n`.

> On rappelle que `n % 2` renvoie le reste dans la division de `n` par `2`, et que s'il est nul, c'est que `n` est un nombre pair.

!!! example "Exemple"

    ```pycon
    >>> syracuse(7)
    [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    >>> syracuse(3)
    [3, 10, 5, 16, 8, 4, 2, 1]
    >>> syracuse(1)
    [1]
    ```


```python
    --8<-- "./docs/exercices/1-facile/1750-syracuse/exo.py"
```

