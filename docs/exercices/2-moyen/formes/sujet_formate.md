

### Formes géométriques ASCII 


```txt title="🎨 Un rectangle 3×5 plein, motif: #"
    #####
    #####
    #####
```

```txt title="🎨 Un triangle creux 5×5, motif: Y"
    Y
    YY
    Y Y
    Y  Y
    YYYYY
```

Dans cet exercice, on travaille avec des listes de chaines de caractères pour représenter des dessins.

- Chaque ligne d'un dessin sera une chaine de caractères non vide.
- Un dessin sera une liste non vide de lignes.

!!! info "Lignes et dessins, dans cet exercice"
    -  `ligne_pleine` et `ligne_creuse` sont des fonctions qui renvoient une ligne que l'on peut afficher avec `#!py print`
    - `rectangle` et `triangle` en version `creux` ou `plein` sont des fonctions qui renvoient un dessin (une liste de lignes) que l'on peut afficher avec `dessine`.

Compléter le code suivant afin de disposer des fonctions indiquées. On utilisera les fonctions simples dans les fonctions élaborées. Vous n'avez qu'à compléter les fonctions `ligne`, `rectangle` et `triangle` dans chacune des deux versions. Le paramètre `motif` sera une chaine de caractères de longueur 1.

!!! tip "Décommenter bloc par bloc les assertions"
    Le premier bloc d'assertions est actif. Il permet de tester la fonction `ligne_pleine`.

    Quand vous avez réussi, vous pouvez décommenter le bloc suivant d'assertions.
    Pour cela, il suffit de déplacer la ligne `"""` sous le bloc.

!!! example "Exemples"

    ```pycon
    >>> print(ligne_pleine('M', 1))
    M
    >>> print(ligne_pleine('#', 5))
    #####
    >>> print(ligne_creuse('X', 5))
    X   X
    >>> print(ligne_creuse('M', 1))
    M
    ```

    ```pycon
    >>> dessine(rectangle_plein('A', 3, 5))
    AAAAA
    AAAAA
    AAAAA
    >>> dessine(rectangle_creux('O', 3, 5))
    OOOOO
    O   O
    OOOOO
    >>> dessine(rectangle_creux('O', 1, 5))
    OOOOO
    ```

    ```pycon
    >>> dessine(triangle_plein('T', 5))
    T
    TT
    TTT
    TTTT
    TTTTT
    >>> dessine(triangle_creux('F', 5))
    F
    FF
    F F
    F  F
    FFFFF
    >>> dessine(triangle_creux('K', 1))
    K
    ```


```python
    --8<-- "./docs/exercices/2-moyen/formes/exo.py"
```

