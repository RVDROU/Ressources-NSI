

### Sortie de labyrinthe 


![Labyrinthe de buisson](labyrinthe/images/clipart1988947.png)

[//]: # (https://www.clipartmax.com/middle/m2i8b1d3G6Z5Z5H7_bush-maze-hedge/)  

Un labyrinthe rectangulaire délimité et entouré par des buissons peut être schématisé par un tableau 2D : une liste de listes d'entiers égaux à `0` ou `1`.

- Les `1` désignent des buissons dans lesquels on s'entrave.
- Les `0` désignent des emplacements libres, où l'on peut circuler vers toute case libre immédiatement au Nord, au Sud, à l'Est ou à l'Ouest.
- Il y a au moins trois lignes et trois colonnes.
    - La première et la dernière ligne sont remplies de `1`.
    - La première et la dernière colonne sont remplies de `1`.
- Le départ est sur la deuxième ligne, deuxième colonne. Cette case est libre.
- La sortie est sur l'avant-dernière ligne, avant-dernière deuxième colonne.


Un chemin est décrit par une chaine de caractères composée de lettres parmi `"NSEO"`.

- Le Nord (`N`), c'est vers le haut du tableau ; $-1$ pour la ligne, même colonne.
- Le Sud (`S`), c'est vers le bas du tableau ; $+1$ pour la ligne, même colonne.
- L'Est (`E`), c'est vers la droite du tableau ; même ligne, $+1$ pour la colonne.
- L'Ouest (`O`), c'est vers la gauche du tableau ; même ligne, $-1$ pour la colonne.



Écrire une fonction telle que `verifie(labyrinthe, chemin)` renvoie un booléen, la réponse à la question « La description `chemin` permet-elle d'aller du départ à la sortie du `labyrinthe` sans passer deux fois sur la même case, ni passer par des buissons ? »

La fonction pourra modifier `labyrinthe` à loisir.

Code à compléter :



!!! example "Exemples"

    ```python
    labyrinthe  = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    chemin_1 = "EEEEES"
    chemin_2 = "SSSSSEENNNEEEEEEESSOOOOSSSEEEESS"

    import copy
    labyrinthe_1 = copy.deepcopy(labyrinthe)
    labyrinthe_2 = copy.deepcopy(labyrinthe)

    assert not verifie(labyrinthe_1, chemin_1)
    assert     verifie(labyrinthe_2, chemin_2)
    ```

    ![labyrinthe](labyrinthe/images/labyrinthe.svg)


```python
    --8<-- "./docs/exercices/2-moyen/labyrinthe/exo.py"
```

