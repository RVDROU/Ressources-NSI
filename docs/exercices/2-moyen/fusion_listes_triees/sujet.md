---
author: BNS2022-10.2, puis Franck Chambon
title: Fusion de listes triées
search:
    - exclude: True
tags:
  - a_trou
  - tri
---
La fonction `fusion` prend deux listes `liste_a`, `liste_b` d'entiers triées par ordre croissant et les fusionne en une seule liste triée `liste_triee` qu'elle renvoie.

> Pour cet exercice, on n'utilisera ni `sort`, ni `sorted`.

Compléter le code :

{{ py_sujet('exo') }}

!!! example "Exemples"

    ```pycon
    >>> fusion([1, 6, 10], [0, 7, 8, 9])
    [0, 1, 6, 7, 8, 9, 10]
    ```

    ```pycon
    >>> fusion([1, 6, 10], [])
    [1, 6, 10]
    ```

    ```pycon
    >>> fusion([], [0, 7, 8, 9])
    [0, 7, 8, 9]
    ```

{{ IDE('exo') }}
