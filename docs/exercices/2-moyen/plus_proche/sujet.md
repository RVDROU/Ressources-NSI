---
author: BNS2022-36.2 puis Sébastien HOARAU
title: Le plus proche
search:
    - exclude: True
tag:
    - boucle
    - float
    - indice
---
Nous souhaitons programmer une fonction qui, étant donné une liste de points du plan à coordonnées entières, donne celui qui est le plus proche d'un point de départ.

Les points sont donnés sous la forme d'un tuple de deux entiers.
La liste des points à traiter est donc un tableau de tuples.

La distance utilisée est la distance euclidienne, dont on rappelle la définition. La distance euclidienne entre deux points du plan de coordonnées $(x_1;y_1)$ et $(x_2;y_2)$
est donnée par la formule :

$$d=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$$

!!! note "Indication"

    Si la variable `point` référence notre couple de coordonnées, alors le _décompactage_ permet de donner un nom simple aux composantes `point[0]` et `point[1]` :

    ```python
    x, y = point
    ```

    Vous pouvez utiliser cette astuce dans votre solution.


Nous disposons d'une fonction `distance` et d'une fonction `plus_proche` dans l'IDE suivant. Compléter comme il se doit et tester.

!!! example "Exemples"

    ```pycon
    >>> plus_proche([(7, 9), (2, 5), (5, 2)], (0, 0))
    (2, 5)
    >>> plus_proche([(7, 9), (2, 5), (5, 2)], (7, 9))
    (7, 9)
    ```

{{ IDE('exo') }}
