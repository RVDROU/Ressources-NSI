

### Énumération des expressions bien parenthésées 


!!! info "Expression bien parenthésée"
    Une expression bien parenthésée est une chaine de caractères composée d'autant de `(` que de `)` et où chaque parenthèse ouvrante est placée avant la fermante qui lui correspond.

    - `()(())` et `((()))()` sont bien parenthésées
    - `)()(` et `())(()` ne sont pas bien parenthésées.

- Pour $2$ paires de parenthèses, il y a $2$ expressions bien parenthésées.
    - `()()`
    - `(())`
- Pour $3$ paires de parenthèses, il y a $5$ expressions bien parenthésées.
    - `()()()`
    - `(())()`
    - `()(())`
    - `(()())`
    - `((()))`

On admettra que le nombres d'expressions bien parenthésées contenant $n$ paires de parenthèses est le nombre de Catalan $C_n$ que l'on peut calculer, par exemple, avec la formule suivante :

$$C_n = \begin{cases}
1                                & \quad \text{ si } n = 0\\
C_{n-1}×\dfrac{2(2n - 1)}{n + 1}  & \quad \text{ si } n > 0\\
\end{cases}$$

**Objectif** : Écrire une fonction telle que `catalan(n)` renvoie le nombre de Catalan d'indice `n`.

- On utilisera la liste `catalan_mem` pour conserver en mémoire les résultats, ce qui permet un accès ultérieur sans calcul.
- On utilisera la variable `catalan_i` pour désigner $C_i$ et `catalan_im1` pour désigner $C_{i-1}$.
- On sera capable de **justifier à l'oral** le commentaire placé dans le code.
- On complètera le code :



!!! example "Exemples"

    ```pycon
    >>> catalan(2)
    2
    >>> catalan(3)
    5
    >>> catalan(5)
    42
    ```


```python
    --8<-- "./docs/exercices/2-moyen/nb_catalan_1/exo.py"
```

