---
author: Franck Chambon
title: Carrés magiques normaux d'ordre n
search:
    - exclude: True
tags:
  - maths+
  - boucle
  - grille
---
Un carré magique normal d'ordre $n$ est une grille carrée remplie de tous les entiers de $1$ à $n^2$, telle que les sommes suivantes sont égales :

- la somme des nombres de chaque ligne,
- la somme des nombres de chaque colonne,
- la somme des nombres des deux diagonales.

!!! info "Carré magique d'ordre $3$"

    ```python
    ex_ordre_3 = [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8],
    ]
    ```

    Voici un exemple avec tous les entiers de $1$ à 9$.

    - la somme de chaque ligne est égale à $15$
        - $2+7+6 = 15$
        - $9+5+1 = 15$
        - $4+3+8 = 15$
    - la somme de chaque colonne est égale à $15$ ;
        - $2+9+4 = 15$
        - $7+5+3 = 15$
        - $6+1+8 = 15$
    - la somme de chaque diagonale est égale à $15$.
        - $2+5+8 = 15$
        - $4+5+6 = 15$


!!! info "Carré magique d'ordre $4$"

    ```python
    ex_ordre_4 = [
        [16,  3,  2, 13],
        [ 5, 10, 11,  8],
        [ 9,  6,  7, 12],
        [ 4, 15, 14,  1], 
    ]
    ```
    Ce carré magique était connu du peintre allemand Albrecht Dürer, qui l'a inclus dans sa gravure _Melencolia_.


Écrire une fonction telle que `est_carre_magique(carre)` renvoie un booléen, la réponse à la question : `carre` est-il un carré magique normal ?

On garantit que `carre` est un tableau 2D de forme carrée, rempli d'entiers ; il y a autant de lignes que de colonnes et toutes les lignes ont le même nombre de colonnes.

!!! example "Exemples"

    ```pycon
    >>> ex_ordre_3 = [
    ...     [2, 7, 6],
    ...     [9, 5, 1],
    ...     [4, 3, 8],
    ... ]
    >>> est_carre_magique(ex_ordre_3)
    True
    ```
    ```pycon
    >>> contre_ex_ordre_2 = [
    ...     [2, 2],
    ...     [2, 2],
    ... ]
    >>> est_carre_magique(contre_ex_ordre_2)
    False
    ```
    ```pycon
    >>> ex_ordre_4 = [
    ...     [16,  3,  2, 13],
    ...     [ 5, 10, 11,  8],
    ...     [ 9,  6,  7, 12],
    ...     [ 4, 15, 14,  1], 
    ... ]
    >>> est_carre_magique(ex_ordre_4)
    True
    ```


{{ IDE('exo') }}

??? tip "Indice 1"
    En utilisant la formule $1+2+3+\cdots+n^2 = \dfrac{n^2(n^2+1)}{2}$, il est possible de déterminer la somme commune d'un carré magique normal d'ordre $n$, sans même avoir lu une seule ligne du tableau.

??? tip "Indice 2"
    On pourra procéder par étapes. À chaque test qui échoue, la fonction peut renvoyer `False`.

    À la fin, si tous les critères sont validés, la fonction renvoie `True`.

??? tip "Indice 3"
    Pour vérifier la présence unique des nombres de $1$ à $n^2$, on pourra utiliser un tableau de booléen `deja_vu` de longueur $n^2+1$.

    On pensera à tester au passage que les entiers sont bien de $1$ à $n^2$.
