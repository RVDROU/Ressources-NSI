---
author: Franck Chambon
title: Énumération des chemins de Delannoy
search:
    - exclude: True
tags:
  - maths+
  - récursivité
  - dictionnaire
  - mémo
  - a_trou
---
Dans une grille de taille $n×m$, on souhaite compter tous les chemins allant du coin inférieur gauche (au Sud-Ouest) vers le coin supérieur droit (au Nord-Est).

Les seuls mouvements autorisés sont :

- ↑ Aller au Nord d'une unité.
- → Aller à l'Est d'une unité.
- ↗ Aller au Nord-Est en diagonale, sur le prochain nœud.

!!! info "Les chemins pour aller de $(0, 0)$ à $(3, 3)$"

    ![](images/chemin_0.svg)
    ![](images/chemin_1.svg)
    ![](images/chemin_2.svg)
    ![](images/chemin_3.svg)
    ![](images/chemin_4.svg)
    ![](images/chemin_5.svg)
    ![](images/chemin_6.svg)
    ![](images/chemin_7.svg)
    ![](images/chemin_8.svg)
    ![](images/chemin_9.svg)
    ![](images/chemin_10.svg)
    ![](images/chemin_11.svg)
    ![](images/chemin_12.svg)
    ![](images/chemin_13.svg)
    ![](images/chemin_14.svg)
    ![](images/chemin_15.svg)
    ![](images/chemin_16.svg)
    ![](images/chemin_17.svg)
    ![](images/chemin_18.svg)
    ![](images/chemin_19.svg)
    ![](images/chemin_20.svg)
    ![](images/chemin_21.svg)
    ![](images/chemin_22.svg)
    ![](images/chemin_23.svg)
    ![](images/chemin_24.svg)
    ![](images/chemin_25.svg)
    ![](images/chemin_26.svg)
    ![](images/chemin_27.svg)
    ![](images/chemin_28.svg)
    ![](images/chemin_29.svg)
    ![](images/chemin_30.svg)
    ![](images/chemin_31.svg)
    ![](images/chemin_32.svg)
    ![](images/chemin_33.svg)
    ![](images/chemin_34.svg)
    ![](images/chemin_35.svg)
    ![](images/chemin_36.svg)
    ![](images/chemin_37.svg)
    ![](images/chemin_38.svg)
    ![](images/chemin_39.svg)
    ![](images/chemin_40.svg)
    ![](images/chemin_41.svg)
    ![](images/chemin_42.svg)
    ![](images/chemin_43.svg)
    ![](images/chemin_44.svg)
    ![](images/chemin_45.svg)
    ![](images/chemin_46.svg)
    ![](images/chemin_47.svg)
    ![](images/chemin_48.svg)
    ![](images/chemin_49.svg)
    ![](images/chemin_50.svg)
    ![](images/chemin_51.svg)
    ![](images/chemin_52.svg)
    ![](images/chemin_53.svg)
    ![](images/chemin_54.svg)
    ![](images/chemin_55.svg)
    ![](images/chemin_56.svg)
    ![](images/chemin_57.svg)
    ![](images/chemin_58.svg)
    ![](images/chemin_59.svg)
    ![](images/chemin_60.svg)
    ![](images/chemin_61.svg)
    ![](images/chemin_62.svg)



Écrire une fonction telle que `delannoy(n, m)` renvoie le nombre de chemins allant de $(0, 0)$ jusqu'à $(n, m)$.

Pour ce faire, on remarquera :

- Si `n` ou `m` est nul,
    - alors le seul chemin est en ligne droite, la réponse est `1`,
- sinon :
    -`n` et `m` sont non nuls et les chemins qui vont en `(n, m)` se répartissent en trois catégories :
        - ceux qui venaient de `(n - 1, m    )`,
        - ceux qui venaient de `(n    , m - 1)`,
        - ceux qui venaient de `(n - 1, m - 1)`,
    - ces trois catégories sont distinctes et se comptent bien par récursivité.
- On utilisera un dictionnaire pour mémoriser les résultats intermédiaires.
- On complètera le code :

{{ py_sujet('exo') }}

!!! example "Exemples"

    ```pycon
    >>> delannoy(3, 3)
    63
    >>> delannoy(2, 1)
    5
    ```

{{ IDE('exo') }}
