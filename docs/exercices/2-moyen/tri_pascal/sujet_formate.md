

### Triangle de Pascal 


On cherche à construire le triangle de Pascal.

!!! info "Le triangle de Pascal"
    Dans ce tableau de forme triangulaire, chaque ligne commence et se termine par le nombre $1$.
    
    Par ailleurs, la valeur qui occupe une case située à l'intérieur du tableau s'obtient en ajoutant les valeurs des deux cases situées juste au-dessus et au-dessus à gauche, comme l'indique la figure suivante :

    | Colonnes : | 0 | 1 | 2 | 3 | 4 | 5 |
    | :-------: |:-:|:-:|:-:|:-:|:-:|:-:|
    | ligne 0 : |$1$|   |   |   |   |   |
    | ligne 1 : |$1$|$1$|   |   |   |   |
    | ligne 2 : |$1$|$2$|$1$|   |   |   |
    | ligne 3 : |$1$|$3$|$3$|$1$|   |   |
    | ligne 4 : |$1$|$4$|$\mathbf{6}$|$\mathbf{4}$|$1$|   |
    | ligne 5 : |$1$|$5$|$10$|$\mathbf{10}$|$5$|$1$|

    Le second $10$ s'obtient avec $6$ en haut à gauche, plus $4$ juste au-dessus ; comme pour tous les nombres du tableau, sauf les $1$ qui sont placés par définition.

**Objectif** : Écrire une fonction telle que `pascal(n)` renvoie la liste correspondant au triangle de Pascal de la ligne `0` à la ligne `n`. **Il y a $(n+1)$ lignes.**

Compléter le code suivant :



!!! example "Exemples"

    ```pycon
    >>> pascal(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    >>> pascal(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    ```


```python
    --8<-- "./docs/exercices/2-moyen/tri_pascal/exo.py"
```

