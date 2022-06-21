

### Nombres de chemins dans une grille 


Dans une grille de taille $n×m$, on souhaite compter tous les chemins allant du coin inférieur gauche (au Sud-Ouest) vers le coin supérieur droit (au Nord-Est).

Les seuls mouvements autorisés sont :

- ↑ Aller au Nord d'une unité.
- → Aller à l'Est d'une unité.

!!! info "Les chemins pour aller de $(0, 0)$ à $(4, 3)$"

    Ceux passant par $(3, 3)$, il y en a 20.

    ![](nb_chemins_grille/images/chemin_0.svg)
    ![](nb_chemins_grille/images/chemin_1.svg)
    ![](nb_chemins_grille/images/chemin_2.svg)
    ![](nb_chemins_grille/images/chemin_3.svg)
    ![](nb_chemins_grille/images/chemin_4.svg)
    ![](nb_chemins_grille/images/chemin_5.svg)
    ![](nb_chemins_grille/images/chemin_6.svg)
    ![](nb_chemins_grille/images/chemin_7.svg)
    ![](nb_chemins_grille/images/chemin_8.svg)
    ![](nb_chemins_grille/images/chemin_9.svg)
    ![](nb_chemins_grille/images/chemin_10.svg)
    ![](nb_chemins_grille/images/chemin_11.svg)
    ![](nb_chemins_grille/images/chemin_12.svg)
    ![](nb_chemins_grille/images/chemin_13.svg)
    ![](nb_chemins_grille/images/chemin_14.svg)
    ![](nb_chemins_grille/images/chemin_15.svg)
    ![](nb_chemins_grille/images/chemin_16.svg)
    ![](nb_chemins_grille/images/chemin_17.svg)
    ![](nb_chemins_grille/images/chemin_18.svg)
    ![](nb_chemins_grille/images/chemin_19.svg)

    Ceux passant par $(4, 2)$, il y en a 15.

    ![](nb_chemins_grille/images/chemin_20.svg)
    ![](nb_chemins_grille/images/chemin_21.svg)
    ![](nb_chemins_grille/images/chemin_22.svg)
    ![](nb_chemins_grille/images/chemin_23.svg)
    ![](nb_chemins_grille/images/chemin_24.svg)
    ![](nb_chemins_grille/images/chemin_25.svg)
    ![](nb_chemins_grille/images/chemin_26.svg)
    ![](nb_chemins_grille/images/chemin_27.svg)
    ![](nb_chemins_grille/images/chemin_28.svg)
    ![](nb_chemins_grille/images/chemin_29.svg)
    ![](nb_chemins_grille/images/chemin_30.svg)
    ![](nb_chemins_grille/images/chemin_31.svg)
    ![](nb_chemins_grille/images/chemin_32.svg)
    ![](nb_chemins_grille/images/chemin_33.svg)
    ![](nb_chemins_grille/images/chemin_34.svg)

Écrire une fonction telle que `nb_chemins(n, m)` renvoie le nombre de chemins allant de $(0, 0)$ jusqu'à $(n, m)$.

Pour ce faire, on remarquera :

- Si `n` ou `m` est nul,
    - alors le seul chemin est en ligne droite, la réponse est `1`,
- sinon :
    - `n` et `m` sont non nuls et les chemins qui vont en `(n, m)` se répartissent en deux catégories :
        - ceux qui venaient de `(n - 1, m    )`,
        - ceux qui venaient de `(n    , m - 1)`,
    - ces deux catégories sont distinctes et se comptent bien par récursivité.
- On utilisera un dictionnaire pour mémoriser les résultats intermédiaires.
- On complètera le code :



!!! example "Exemples"

    ```pycon
    >>> nb_chemins(3, 3)
    20
    >>> nb_chemins(4, 2)
    15
    >>> nb_chemins(4, 3)
    35
    ```

Contraintes : Ici, $0\leqslant n \leqslant 20$ et $0\leqslant m \leqslant 20$.


```python
    --8<-- "./docs/exercices/3-difficile/nb_chemins_grille/exo.py"
```

