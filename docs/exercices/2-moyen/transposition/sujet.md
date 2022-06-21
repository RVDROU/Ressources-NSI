---
author: Franck Chambon
title: Transposition  de tableau 2D
search:
    - exclude: True
tags:
  - grille
  - compréhension
  - a_trou
---
La transposition d'un tableau à deux dimensions est une opération qui, concrètement, échange le rôle des lignes et des colonnes.

> On l'utilise en mathématiques pour la multiplication de matrices. On l'utilise en infographie pour des transformations d'images.

$$\begin{bmatrix}
0 & \mathbf{1} & 1 & 1\\
1 & \mathbf{0} & 1 & 0\\
0 & \mathbf{0} & 0 & 1\\
\end{bmatrix}$$

La tableau ci-dessus, donne par transposition

$$\begin{bmatrix}
0 & 1 & 0\\
\mathbf{1} & \mathbf{0} & \mathbf{0}\\
1 & 1 & 0\\
1 & 0 & 1\\
\end{bmatrix}$$

> La colonne d'indice 1 est devenue la ligne d'indice 1.

Écrire une fonction `transposition` qui renvoie la transposition d'un tableau à deux dimensions `grille` : une liste Python contenant des listes d'éléments de même type. Pour cela on utilisera des fonctions telles que :

- `nb_lignes(grille)` renvoie le nombre de lignes de la grille ;
- `ligne(grille, i)` renvoie la ligne d'indice `i` de la grille sous forme d'un tableau.
- `nb_colonnes(grille)` renvoie le nombre de colonnes de la grille ;
- `colonne(grille, j)` renvoie la colonne d'indice `j` de la grille sous forme d'un tableau.


On garantit que pour `grille` :

- Il y a au moins une ligne et au moins une colonne.
- Toutes les lignes sont de même longueur.

Compléter le code :

{{ py_sujet('exo') }}

!!! example "Exemples"

    ```pycon
    >>> grille = [
    ...     [0, 1, 1, 1],
    ...     [1, 0, 1, 0],
    ...     [0, 0, 0, 1],
    ... ]
    >>> nb_lignes(grille)
    3
    >>> ligne(grille, 0)
    [0, 1, 1, 1]
    >>> nb_colonnes(grille)
    4
    >>> colonne(grille, 1)
    [1, 0, 0]
    >>> t_grille = [
    ...     [0, 1, 0],
    ...     [1, 0, 0],
    ...     [1, 1, 0],
    ...     [1, 0, 1],
    ... ]
    >>> transposition(grille) == t_grille
    True
    >>> transposition(t_grille) == grille
    True
    ```

    ```pycon
    >>> grille = [
    ...     ['#', '#', '#', '#', '#'],
    ...     ['#', '#', '#', '#', '#'],
    ...     ['.', '.', '#', '#', '#'],
    ...     ['#', '.', '#', '#', '#'],
    ... ]
    >>> nb_lignes(grille)
    4
    >>> ligne(grille, 3)
    ['#', '.', '#', '#', '#']
    >>> nb_colonnes(grille)
    5
    >>> colonne(grille, 0)
    ['#', '#', '.', '#']
    >>> t_grille = [
    ...     ['#', '#', '.', '#'],
    ...     ['#', '#', '.', '.'],
    ...     ['#', '#', '#', '#'],
    ...     ['#', '#', '#', '#'],
    ...     ['#', '#', '#', '#'],
    ... ]
    >>> transposition(grille) == t_grille
    True
    >>> transposition(t_grille) == grille
    True
    ```

{{ IDE('exo') }}

