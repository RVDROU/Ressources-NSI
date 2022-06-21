

### Tableau de 0 et 1 


```

Tant que la zone non triée n'est pas réduite à un seul élément, on regarde son premier
élément :

- si cet élément vaut 0, on considère qu'il appartient désormais à la zone ne contenant que des 0 ;
- si cet élément vaut 1, il est échangé avec le dernier élément de la zone non triée et on considère alors qu'il appartient à la zone ne contenant que des 1.

Dans tous les cas, la longueur de la zone non triée diminue de 1.

!!! example "Exemples"

    ```pycon
    >>> tableau1 = [0, 1, 0, 1, 0, 1, 0]
    >>> separe(tableau1)
    >>> tableau1
    [0, 0, 0, 0, 1, 1, 1]
    ```
    ```pycon    
    >>> tableau2 = [1, 1, 1, 0, 0, 0]
    >>> separe(tableau2)
    >>> tableau2
    [0, 0, 0, 1, 1, 1]
    ```


```python
    --8<-- "./docs/exercices/2-moyen/tableau_0_1/exo.py"
```


