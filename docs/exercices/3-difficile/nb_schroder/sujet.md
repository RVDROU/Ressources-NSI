---
author: Franck Chambon
title: Énumération des chemins de Schröder
search:
    - exclude: True
tags:
  - maths
  - récursivité
  - mémo
  - a_trou
---
Pour aller de $(0, 0)$ à $(2n, 0)$, en restant au-dessus ou sur l'axe des abscisses, avec des mouvements

- ↗ Nord-Est, donc suivi plus tard d'un Sud-Est ↘
- ↘ Sud-Est, qui est précédé d'un ↗ Nord-Est correspondant
- → Est, de deux unités à la fois

Chaque paire (↗, ↘) est associée à un déplacement de deux unités vers l'Est. Ainsi, un chemin de Schröder fait globalement un déplacement horizontal d'un nombre pair d'unités, que l'on note $2n$.

Objectif : Écrire une fonction telle que `schroder(n)` renvoie le nombre de chemins de Schröder allant de $(0, 0)$ à $(2n, 0)$.


!!! done "Chemins de Schröder de longueur $2×2$"

    Il y en a 6.

    ![](images/2_chemin_0.svg)
    ![](images/2_chemin_1.svg)
    ![](images/2_chemin_2.svg)
    ![](images/2_chemin_3.svg)
    ![](images/2_chemin_4.svg)
    ![](images/2_chemin_5.svg)

!!! done "Chemins de Schröder de longueur $2×3$"

    Il y en a 22.

    ![](images/3_chemin_0.svg)
    ![](images/3_chemin_1.svg)
    ![](images/3_chemin_2.svg)
    ![](images/3_chemin_3.svg)
    ![](images/3_chemin_4.svg)
    ![](images/3_chemin_5.svg)
    ![](images/3_chemin_6.svg)
    ![](images/3_chemin_7.svg)
    ![](images/3_chemin_8.svg)
    ![](images/3_chemin_9.svg)
    ![](images/3_chemin_10.svg)
    ![](images/3_chemin_11.svg)
    ![](images/3_chemin_12.svg)
    ![](images/3_chemin_13.svg)
    ![](images/3_chemin_14.svg)
    ![](images/3_chemin_15.svg)
    ![](images/3_chemin_16.svg)
    ![](images/3_chemin_17.svg)
    ![](images/3_chemin_18.svg)
    ![](images/3_chemin_19.svg)
    ![](images/3_chemin_20.svg)
    ![](images/3_chemin_21.svg)

!!! info "Formule"

    On admettra qu'une formule pour calculer ces nombres $S_n$ est :

    - $S_0 = 1$, $S_1 = 2$
    - $(n+1)S_n = (6n-3)S_{n-1} - (n-2)S_{n-2}$, pour $n>1$.

On complètera le code :

{{ py_sujet('exo') }}

!!! example "Exemples"

    ```pycon
    >>> schroder(2)
    6
    >>> schroder(3)
    22
    >>> schroder(4)
    90
    ```

:warning: La fonction doit renvoyer un nombre **entier**.

{{ IDE('exo') }}
