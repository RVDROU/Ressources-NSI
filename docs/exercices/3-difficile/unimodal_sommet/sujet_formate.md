

### Sommet d'un tableau unimodal 



!!! info "Algorithme naïf"

   Il est très simple de déterminer le sommet en parcourant de gauche à droite le tableau.

   Notre objectif est de le faire avec un bien meilleur coût.

On complètera le code :



!!! example "Exemples"

    ```pycon

    >>> sommet([1, 2, 0])
    2
    >>> sommet([1, 9, 8, 7])
    9
    >>> sommet([1, 3, 5, 2])
    5
    >>> sommet([1, 2, 3, 4, 5, 4, 3, 2, 1])
    5
    >>> sommet([1, 2, 3, 4, 3, 2, 1, 0, -1, -2])
    4
    ```


```python
    --8<-- "./docs/exercices/3-difficile/unimodal_sommet/exo.py"
```

