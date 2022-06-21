---
author: BNS2022-6.2, puis Franck Chambon & Sébastien HOARAU
title: texte inclus
search:
    - exclude: True
tags:
  - a_trou
---
L'ADN peut être représenté par une séquence de lettres dans `"ATGC"`.

- Un **brin** est un petit morceau d'ADN, que l'on retrouve parfois dans
- un **gène** qui est une grande séquence d'ADN.

La fonction `est_inclus` prend en paramètres deux chaines de caractères `brin` et `gene` et renvoie la réponse, un booléen, à la question « Retrouve-t-on `brin` inclus dans `gene` ? ».

Cette fonction utilise une fonction auxiliaire : `est_inclus_a_partir_de(extrait, chaine, position)` qui renvoie `True` si on retrouve `extrait` dans `chaine` à partir de `position` dans `chaine` et `False` sinon.

Compléter le code Python ci-dessous.

{{ py_sujet('exo') }}

!!! example "Exemples"

    ```pycon
    >>> est_inclus("AATC", "GTACAAATCTTGCC")
    True
    >>> est_inclus("AGTC", "GTACAAATCTTGCC")
    False
    >>> est_inclus("AGTC", "GTACAAATCTTGCA")
    False
    >>> est_inclus("AGTC", "GTACAAATCTAGTC")
    True
    ```

{{ IDE('exo') }}
