

### Suite de Conway 


Dans la suite mathématique _Look and say_, inventée en 1986 par le mathématicien John Horton Conway, un terme se détermine en annonçant les chiffres formant le terme précédent.

$$\begin{matrix}1\\11\\21\\1211\\111221\\312211\end{matrix}$$

Explication :

- à partir de $111221$,
- on lit $111\,22\,1$,
- soit trois $1$, puis deux $2$, et un $1$,
- d'où $31\,22\,11$ pour la ligne suivante.

On peut vérifier que la ligne suivante est $13112221$.

Pour simplifier le code, on va modéliser cette suite par la liste des chiffres.

```python
LIGNE_1 = [1]
LIGNE_2 = [1, 1]
LIGNE_3 = [2, 1]
LIGNE_4 = [1, 2, 1, 1]
LIGNE_5 = [1, 1, 1, 2, 2, 1]
LIGNE_6 = [3, 1, 2, 2, 1, 1]
LIGNE_7 = [1, 3, 1, 1, 2, 2, 2, 1]
```

Écrire une fonction telle que `conway_suivante(ligne)` renvoie, sous forme de liste, la ligne suivante après `ligne`. Ceci pourrait permettre de faire des appels récursifs.

Code à compléter :



!!! example "Exemples"

    ```python
    >>> conway_suivante([3, 1, 2, 2, 1, 1])
    [1, 3, 1, 1, 2, 2, 2, 1]
    >>> conway_suivante([1, 3, 1, 1, 2, 2, 2, 1])
    [1, 1, 1, 3, 2, 1, 3, 2, 1, 1]
    ```


```python
    --8<-- "./docs/exercices/2-moyen/conway/exo.py"
```


