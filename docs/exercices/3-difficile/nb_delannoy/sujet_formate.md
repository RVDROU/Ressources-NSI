

### Énumération des chemins de Delannoy 


Dans une grille de taille $n×m$, on souhaite compter tous les chemins allant du coin inférieur gauche (au Sud-Ouest) vers le coin supérieur droit (au Nord-Est).

Les seuls mouvements autorisés sont :

- ↑ Aller au Nord d'une unité.
- → Aller à l'Est d'une unité.
- ↗ Aller au Nord-Est en diagonale, sur le prochain nœud.

!!! info "Les chemins pour aller de $(0, 0)$ à $(3, 3)$"

    ![](nb_delannoy/images/chemin_0.svg)
    ![](nb_delannoy/images/chemin_1.svg)
    ![](nb_delannoy/images/chemin_2.svg)
    ![](nb_delannoy/images/chemin_3.svg)
    ![](nb_delannoy/images/chemin_4.svg)
    ![](nb_delannoy/images/chemin_5.svg)
    ![](nb_delannoy/images/chemin_6.svg)
    ![](nb_delannoy/images/chemin_7.svg)
    ![](nb_delannoy/images/chemin_8.svg)
    ![](nb_delannoy/images/chemin_9.svg)
    ![](nb_delannoy/images/chemin_10.svg)
    ![](nb_delannoy/images/chemin_11.svg)
    ![](nb_delannoy/images/chemin_12.svg)
    ![](nb_delannoy/images/chemin_13.svg)
    ![](nb_delannoy/images/chemin_14.svg)
    ![](nb_delannoy/images/chemin_15.svg)
    ![](nb_delannoy/images/chemin_16.svg)
    ![](nb_delannoy/images/chemin_17.svg)
    ![](nb_delannoy/images/chemin_18.svg)
    ![](nb_delannoy/images/chemin_19.svg)
    ![](nb_delannoy/images/chemin_20.svg)
    ![](nb_delannoy/images/chemin_21.svg)
    ![](nb_delannoy/images/chemin_22.svg)
    ![](nb_delannoy/images/chemin_23.svg)
    ![](nb_delannoy/images/chemin_24.svg)
    ![](nb_delannoy/images/chemin_25.svg)
    ![](nb_delannoy/images/chemin_26.svg)
    ![](nb_delannoy/images/chemin_27.svg)
    ![](nb_delannoy/images/chemin_28.svg)
    ![](nb_delannoy/images/chemin_29.svg)
    ![](nb_delannoy/images/chemin_30.svg)
    ![](nb_delannoy/images/chemin_31.svg)
    ![](nb_delannoy/images/chemin_32.svg)
    ![](nb_delannoy/images/chemin_33.svg)
    ![](nb_delannoy/images/chemin_34.svg)
    ![](nb_delannoy/images/chemin_35.svg)
    ![](nb_delannoy/images/chemin_36.svg)
    ![](nb_delannoy/images/chemin_37.svg)
    ![](nb_delannoy/images/chemin_38.svg)
    ![](nb_delannoy/images/chemin_39.svg)
    ![](nb_delannoy/images/chemin_40.svg)
    ![](nb_delannoy/images/chemin_41.svg)
    ![](nb_delannoy/images/chemin_42.svg)
    ![](nb_delannoy/images/chemin_43.svg)
    ![](nb_delannoy/images/chemin_44.svg)
    ![](nb_delannoy/images/chemin_45.svg)
    ![](nb_delannoy/images/chemin_46.svg)
    ![](nb_delannoy/images/chemin_47.svg)
    ![](nb_delannoy/images/chemin_48.svg)
    ![](nb_delannoy/images/chemin_49.svg)
    ![](nb_delannoy/images/chemin_50.svg)
    ![](nb_delannoy/images/chemin_51.svg)
    ![](nb_delannoy/images/chemin_52.svg)
    ![](nb_delannoy/images/chemin_53.svg)
    ![](nb_delannoy/images/chemin_54.svg)
    ![](nb_delannoy/images/chemin_55.svg)
    ![](nb_delannoy/images/chemin_56.svg)
    ![](nb_delannoy/images/chemin_57.svg)
    ![](nb_delannoy/images/chemin_58.svg)
    ![](nb_delannoy/images/chemin_59.svg)
    ![](nb_delannoy/images/chemin_60.svg)
    ![](nb_delannoy/images/chemin_61.svg)
    ![](nb_delannoy/images/chemin_62.svg)



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



!!! example "Exemples"

    ```pycon
    >>> delannoy(3, 3)
    63
    >>> delannoy(2, 1)
    5
    ```


```python
    --8<-- "./docs/exercices/3-difficile/nb_delannoy/exo.py"
```

