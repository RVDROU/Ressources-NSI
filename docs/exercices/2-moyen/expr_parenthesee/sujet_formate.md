

### Expression parenthésée 


Une expression arithmétique ne comportant que les quatre opérations $+, - , ×, ÷$ peut être représentée sous forme d'arbre binaire. Les nœuds internes sont des opérateurs et les feuilles sont des nombres. Dans un tel arbre, la disposition des nœuds joue le rôle des parenthèses que nous connaissons bien.

- Les nœuds internes (pour les opérateurs binaires) ont tous deux sous arbres non vides : les opérandes.
- Les feuilles rassemblent tous les nombres.

Avec un parcours en profondeur infixe l'arbre binaire ci-dessous, on
peut retrouver l'expression notée habituellement : $3 × (8 + 7) - (2 + 1)$.


![arbre](expr_parenthesee/images/sombre.svg){ .sombre }
![arbre](expr_parenthesee/images/clair.svg){ .clair }


La classe `Noeud` ci-après permet d'implémenter une structure d'arbre binaire.

Compléter la fonction récursive `expression_parenthesee` qui prend en paramètre un objet de la classe `Noeud` et qui renvoie l'expression arithmétique représentée par l'arbre binaire passé en paramètre, sous forme d'une chaine de caractères contenant des parenthèses.



!!! example "Exemple"
    Résultat attendu avec l'arbre ci-dessus :

    ```pycon
    >>> somme_1 = Noeud(Noeud(None, 8, None), '+', Noeud(None, 7, None))
    >>> somme_2 = Noeud(Noeud(None, 2, None), '+', Noeud(None, 1, None))
    >>> produit_1 = Noeud(Noeud(None, 3, None), '*', somme_1)
    >>> expression = Noeud(produit_1, '-', somme_2)
    >>> expression_parenthesee(expression)
    '((3*(8+7))-(2+1))'
    ```

    ```pycon
    >>> feuille = Noeud(None, 5, None)
    >>> expression_parenthesee(feuille)
    '5'
    ```




```python
    --8<-- "./docs/exercices/2-moyen/expr_parenthesee/exo.py"
```

