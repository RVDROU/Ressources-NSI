

### Meilleures apparitions dans un tableau 

---
author: BNS2022-37.2 puis Sébastien Hoarau
title: Meilleures apparitions dans un tableau
search:
    - exclude: True
tag:
    - dictionnaire
    - boucle
--- 
Chaque soir, les auditeurs d'une radio votent en ligne pour leur artiste favori. Ces votes sont stockés dans un tableau.

!!! example "Exemple"

    ```pycon
    >>> urne = ['Oreilles sales', 'Oreilles sales', 'Oreilles sales', 'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba', 'Extra Vomit', 'Lady Baba', 'Extra Vomit']
    >>> depouille(urne)
    {'Oreilles sales': 3, 'Extra Vomit': 4, 'Lady Baba': 3}
    >>> vainqueur(depouille(urne))
    ['Extra Vomit']

    >>> urne_2 = ['Poons', 'DrRed', 'Soleran', 'Mimeen', 'Poons', 'Soleran', 'Mimeen', 'Zajy', 'Soleran', 'DrRed', 'Zajy', 'Kashur', 'Mimeen']
    >>> depouille(urne_2)
    {'Poons': 2, 'DrRed': 2, 'Soleran': 3, 'Mimeen': 3, 'Zajy': 2, 'Kashur': 1}
    >>> sorted(vainqueur(depouille(urne_2)))
    ['Mimeen', 'Soleran']
    ```

La fonction `vainqueur` doit désigner le nom du ou des gagnants. Elle prend en paramètre un dictionnaire dont la structure est celle du dictionnaire renvoyé par la fonction `depouille` et renvoie un tableau. Ce tableau peut donc contenir plusieurs éléments s'il y a des artistes ex aequo.

Compléter les fonctions `depouille` et `vainqueur` fournies dans l'IDE pour qu'elles renvoient les résultats attendus (l'ordre des artistes n'aura pas d'importance).


```python
    --8<-- "./docs/exercices/2-moyen/resultat_vote/exo.py"
```


