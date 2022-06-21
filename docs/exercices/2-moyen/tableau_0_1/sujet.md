---
author: BNS2022-12.2, puis Romain Janvier
title: Tableau de 0 et 1
search:
    - exclude: True
tags:
  - boucle
  - tri
  - a_trou
---
On considère un tableau d'entiers `zeros_et_uns` (type `list` dont les éléments sont des `0` ou des `1`). On se propose de trier ce tableau selon l'algorithme suivant : à chaque étape du tri, le tableau est constitué de trois zones consécutives, la première ne contenant que des `0`,
la seconde n'étant pas triée et la dernière ne contenant que des `1`.

Ci-dessous un schéma de la situation pendant le processus de séparation des 0 et des 1 :

```
debut de zone            fin de zone
    non triée            non triée
           |              |
           v              v
 ------------------------------------
| 0 ... 0 | zone non triée | 1 ... 1 |
 ------------------------------------
```

Tant que la zone non triée n'est pas réduite à un seul élément, on regarde son premier
élément :

- si cet élément vaut 0, on considère qu'il appartient désormais à la zone ne contenant que des 0 ;
- si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on considère alors qu'il appartient à la zone ne contenant que des 1.

Dans tous les cas, la longueur de la zone non triée diminue de 1.

!!! example "Exemples"

    ```pycon
    >>> tableau1 = [0, 1, 0, 1, 0, 1, 0]
    >>> separe(tableau1)
    >>> tableau1
    [0, 0, 0, 0, 1, 1, 1]
    ```
    ```pycon    
    >>> tableau2 = [1, 1, 1, 0, 0, 0]
    >>> separe(tableau2)
    >>> tableau2
    [0, 0, 0, 1, 1, 1]
    ```

{{ IDE('exo') }}

