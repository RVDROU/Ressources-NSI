# Commentaires

## Version classique

{{ py('exo_corr') }}

1. On complète `#!py return resultat` à la fin, ligne 15, c'est la liste des nouveaux chiffres. Elle se construit par accumulation, et elle est initialisée vide à la ligne 4 `#!py resultat = []`.
2. À chaque changement de chiffre,
    - on ajoute à la liste d'abord la quantité `nb_consecutifs`, puis le chiffre `precedent`. En sortie de boucle, on agit comme s'il y avait changement.
    - On met à jour `precedent = chiffre`, et `nb_consecutifs = 1` en comptant ce chiffre juste vu. On remarque qu'à la ligne 3, on n'avait pas encore vu le premier chiffre, donc l'initialisation était à 0.
3. Si le chiffre est le même, on incrémente `nb_consecutifs` de 1.


## Version fonctionnelle

Dans le module `itertools`, il y a une fonction `groupby` qui permet de regrouper par lot, dans un itérable, les termes consécutifs identiques.

```python
from itertools import groupby

def conway_suivante(ligne):
    resultat = []
    for motif, iterable in groupby(ligne):
        resultat.append(sum(1 for chiffre in iterable))
        resultat.append(motif)
    return resultat
```
