

### Anagrammes 


Deux chaînes de caractères **de mêmes longueurs** sont des anagrammes s'il est possible d'écrire l'une en utilisant tous les caractères de l'autre, quitte à les déplacer.

Par exemple les chaînes `chien` et `niche` sont des anagrammes, alors que `louve` et `poule` ne le sont pas.

Déterminer si deux chaînes de caractères sont des anagrammes peut se faire en les comparant après les avoir triées.

On utilise ici une autre approche, récursive :

* si les deux chaînes sont de longueur 1, on renvoie `#!py True` ou `#!py False` selon qu'elles sont égales ou non
* sinon, on teste si le premier caractère de la première se trouve aussi dans la seconde :
    * si oui, on recommence le test sur les deux chaînes dans lesquelles on a retiré la première apparition du caractère testé
    * si non, on renvoie `#!py False`

!!! example "Exemple"

    Pour tester si `chien` et `niche` sont des anagrammes :

    * on observe que `c` est bien dans `niche`
    * on teste si `hien` et `nihe` sont des anagrammes
    * on observe que `h` est bien dans `nihe`
    * on teste si `ien` et `nie` sont des anagrammes
    * ...
    * on observe que `n` et `n` sont égales : on renvoie `#!py True`

Vous devez écrire deux fonctions :

* `supprime_premier(chaine, cible)` renvoie un couple `(present, chaine_sans_cible)` dans lequel `present` est un booléen indiquant si le caractère `cible` est présent dans `chaine` et `chaine_sans_cible` la même chaîne sans la première occurrence de `cible`
* `anagramme(chaine1, chaine2)` renvoie `#!py True` si les deux chaînes sont des anagrammes, `#!py False` sinon

On garantit que les deux chaînes sont non vides.

!!! example "Exemples"

    ```pycon
    >>> supprime_premier('ukulélé', 'u')
    (True, 'kulélé')
    >>> supprime_premier('ukulélé', 'é')
    (True, 'ukullé')
    >>> supprime_premier('ukulélé', 'a')
    (False, 'ukulélé')
    >>> anagrammes('chien', 'niche')
    True
    >>> anagrammes('énergie noire', 'reine ignorée')
    True
    >>> anagrammes('louve', 'poule')
    False
    ```


```python
    --8<-- "./docs/exercices/2-moyen/anagrammes/exo.py"
```

