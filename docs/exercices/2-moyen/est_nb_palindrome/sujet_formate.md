

### Un nombre est-il palindrome ? 


Un mot palindrome peut se lire de la même façon de gauche à droite ou de droite à
gauche : `'esse'`, `'radar'`, et `'non'` sont des mots palindromes.

De même certains nombres sont eux-aussi des palindromes : $33$, $121$, $345543$.

L'objectif de cet exercice est d'obtenir un programme Python permettant de tester si un nombre est un nombre palindrome.

Pour remplir cette tâche, on vous demande de compléter le code des trois fonctions ci-dessous sachant que la fonction `est_nbr_palindrome` s'appuiera sur la fonction `est_palindrome` qui elle-même s'appuiera sur la fonction `inverse_chaine`.

La fonction `inverse_chaine` inverse l'ordre des caractères d'une chaine de caractères `chaine` et renvoie la chaine inversée.

La fonction `est_palindrome` teste si une chaine de caractères `chaine` est un
palindrome. Elle renvoie `True` si c'est le cas et `False` sinon. Cette fonction s'appuie sur la fonction précédente.

La fonction `est_nbr_palindrome` teste si un nombre `nombre` est un palindrome. Elle renvoie `True` si c'est le cas et `False` sinon. Cette fonction s'appuie sur la fonction précédente.

Compléter le code des trois fonctions ci-dessous.



!!! example "Exemples"

    ```pycon
    >>> inverse_chaine('bac')
    'cab'
    >>> est_palindrome('NSI')
    False
    >>> est_palindrome('ISN-NSI')
    True
    >>> est_nbr_palindrome(214312)
    False
    >>> est_nbr_palindrome(213312)
    True
    ```


```python
    --8<-- "./docs/exercices/2-moyen/est_nb_palindrome/exo.py"
```

