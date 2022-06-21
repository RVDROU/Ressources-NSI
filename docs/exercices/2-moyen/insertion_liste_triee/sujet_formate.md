

### Insère dans liste triée 


On considère la fonction `insere` ci-dessous qui prend en argument un entier `a` et une liste `nombres` d'entiers triés par ordre croissant. Cette fonction insère la valeur `a` dans la liste.



Compléter la fonction `insere` ci-dessus.

!!! example "Exemples"

    ```pycon
    >>> exemple_1 = [1, 2, 4, 5]
    >>> insere(3, exemple_1)
    >>> exemple_1
    [1, 2, 3, 4, 5]
    ```

    ```pycon
    >>> exemple_2 = [1, 2, 7, 12, 14, 25]
    >>> insere(7, exemple_2)
    >>> exemple_2
    [1, 2, 7, 7, 12, 14, 25]
    ```

    ```pycon
    >>> exemple_3 = [2, 3, 4]
    >>> insere(1, exemple_3)
    >>> ex_3
    [1, 2, 3, 4]
    ```



```python
    --8<-- "./docs/exercices/2-moyen/insertion_liste_triee/exo.py"
```

