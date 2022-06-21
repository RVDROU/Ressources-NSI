

### Redimensionner un tableau 


On considère un tableau de nombres, une matrice dit-on aussi, de dimensions $l_1 \times h_1$ (largeur $l_1$ et hauteur $h_1$) et l'on souhaite modifier ses dimensions afin de créer un tableau de dimensions $l_2 \times h_2$.

Bien entendu, les deux tableaux contiendront autant de valeurs l'un et l'autre. On garantit donc que l'on aura toujours $l_1 \times h_1 = l_2 \times h_2$.

Par exemple, le tableau de dimensions $4 \times 3$ :

$$
\begin{array}{|c|c|c|c|}
\hline
1&2&3&4\\
\hline
5&6&7&8\\
\hline
9&10&11&12\\
\hline
\end{array}
$$

pourra être transformé en un nouveau tableau de dimensions $6 \times 2$

$$
\begin{array}{|c|c|c|c|c|c|}
\hline
1&2&3&4&5&6\\
\hline
7&8&9&10&11&12\\
\hline
\end{array}
$$

Les tableaux seront représentés par des listes de listes Python. Ainsi les deux tableaux ci-dessus seront représentés par :

```python
tab1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
tab2 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
```

**Démarche**

Il faut tout d'abord créer un nouveau tableau aux bonnes dimensions. Le code Python ci-dessous permet de créer un tableau de
3 lignes sur 5 colonnes rempli de `0`

```python
tab_vide = [[0]*5 for _ in range(3)]
```

Il va ensuite falloir mettre en correspondance les cellules du premier tableau et celles du second.

Pour cela on propose la méthode suivante :

* on crée des coordonnées (par exemple `num_ligne` et `num_colonne`). `num_ligne` est initialisée à `0`, `num_colonne` à `-1`
* on parcourt l'ensemble des lignes et l'ensemble des valeurs du tableau de départ
* A chaque itération :
    * on incrémente `num_colonne` pour passer à une nouvelle colonne
    * on vérifie que `num_colonne` n'est pas égal à la nouvelle largeur
    * si oui, on passe à la ligne suivante (`num_ligne += 1`) et on recommence à la première colonne (`num_colonne = 0`)
    * on insère dans le nouveau tableau la valeur dans la cellule de coordonnées `num_ligne` et `num_colonne` du tableau

Cette méthode est analogue à celle utilisée dans le code ci-dessous permettant de compter les dizaines et les unités entre 0 et 20 :


```python
    --8<-- "./docs/exercices/2-moyen/redimensionner/exo.py"
```



**Au travail !**

Écrire la fonction `redimensionner` prenant en arguments :

* le tableau `tab` à redimensionner sous forme d'une liste de listes
* la nouvelle largeur `nouvelle_largeur`
* la nouvelle hauteur `nouvelle_hauteur`

Cette fonction renverra le tableau redimensionné sous forme d'une liste de listes.

!!! example "Exemples"

    ```pycon
    >>> tab = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    >>> redimensionner(tab, 6, 2)
    [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
    >>> redimensionner(tab, 3, 4)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    ```


```python
    --8<-- "./docs/exercices/2-moyen/redimensionner/exo.py"
```


??? done "Solution"
