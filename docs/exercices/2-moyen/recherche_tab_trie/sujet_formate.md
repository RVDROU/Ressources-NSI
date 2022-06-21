

### Indice dans un tableau trié 


L'objectif de cet exercice est d'écrire une fonction `indice` 

- qui prend en argument :
    - un tableau `valeurs` d'entiers **rangés dans l'ordre croissant**
    - un entier `cible`
- qui renvoie :
    - l'indice de `cible` dans le tableau s'il en fait partie
    - `None` sinon

La fonction `indice` utilisera une fonction `indice_rec` qui sera récursive et qui prendra les mêmes arguments que `indice`, et en plus `debut` et `fin` qui désigneront les indices pour la recherche : de `debut` **inclus** à `fin` **inclus**.

Le tableau `valeurs` pourra être aussi être rempli de chaines de caractères, sans aucun changement à procéder.

On complètera le code :



!!! example "Exemples"

    ```pycon
    >>> nombres = [2, 3, 5, 7, 11, 13, 17]
    >>> indice(nombres, 7)
    3
    >>> indice(nombres, 8) is None
    True
    ```

    ```pycon
    >>> fruits = ["abricot", "kiwi", "mangue", "poire", "pomme"]
    >>> fruits == sorted(fruits)  # le tableau est bien trié
    True
    >>> indice(fruits, "kiwi")
    1
    >>> indice(fruits, "cerise") is None
    True
    ```


```python
    --8<-- "./docs/exercices/2-moyen/recherche_tab_trie/exo.py"
```

