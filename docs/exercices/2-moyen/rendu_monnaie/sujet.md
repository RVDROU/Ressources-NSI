---
author: BNS2022-1.2, puis Franck Chambon et Romain JANVIER
title: Rendu de monnaie
search:
    - exclude: True
tags:
  - a_trou
  - glouton
  - récursivité
---
On s'intéresse à un algorithme récursif qui permet de rendre la monnaie à partir d'une liste donnée de valeurs de pièces et de billets.

Le système monétaire est donné sous forme d'une liste décroissante fixée :

```python
pieces = [100, 50, 20, 10, 5, 2, 1]
```

On supposera qu'il n'y a pas de limitation quant à leur nombre.

On cherche à donner la liste de pièces à rendre pour une somme donnée en argument. Compléter le code Python ci-dessous de la fonction `rendu_monnaie` qui implémente cet algorithme et renvoie la liste des pièces à rendre. La fonction prend un deuxième entier `i` qui correspond à l'indice de la pièce actuellement considérée. Par défaut, il vaut `0` et peut donc être omis lors des tests.

Compléter le code :

{{ py_sujet('exo') }}

!!! example "Exemples"

    ```pycon
    >>> rendu_monnaie(68)
    [50, 10, 5, 2, 1]
    >>> rendu_monnaie(291)
    [100, 100, 50, 20, 20, 1]
    ```

{{ IDE('exo') }}

