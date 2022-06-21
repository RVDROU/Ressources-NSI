# Commentaires

{{ py('exo_corr', 0, "# TESTS") }}

On utilise par commodité les variables `VIDE` et `EAU` définies.

Dès la première ligne, on indique dans le `sol` que l'eau s'est écoulée jusqu'à cette cellule. Cette action empêchera de reconsidérer des cellules déjà visitées.

On teste ensuite le cas de base de la récursivité : la profondeur de la cellule actuelle est-elle égale à la profondeur visée ? Si oui, on renvoie `True`.

Dans le cas contraire, on explore successivement les trois directions (bas, gauche, droite) :

* Pour chacune, on vérifie tout d'abord que la cellule est vide

* Si c'est le cas, on teste alors le retour de l'appel `percolation(sol, nouveau_i, nouveau_j, prof_max)`. S'il vaut `True`, on renvoie directement `True`

* Si aucune des explorations n'a renvoyé `True`, on ne peut pas atteindre la profondeur souhaitée : on renvoie `False`
