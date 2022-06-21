# Commentaires

{{ py_sujet('exo_corr') }}

Si `e` est une feuille, on souhaite renvoyer la valeur sans parenthèse, donc on renvoie `#!py str(e.valeur)` une chaine de caractères.

Sinon, on concatène du texte avec l'opérateur `+` :

- Une parenthèse ouvrante.
- L'expression parenthésée du sous-arbre à gauche `e.gauche`
- L'opérateur sous forme de texte.
- L'expression parenthésée du sous-arbre à droite `e.droite`
- Une parenthèse fermante.

On utilise ici une contre-oblique pour sauter des lignes.

Si l'expression renvoyée était incluse dans des parenthèses, ou crochet, ou accolades, ces contre-obliques auraient été inutiles.

