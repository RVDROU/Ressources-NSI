---
author: BNS2022-11.2, puis Romain Janvier
title: Code de César
search:
    - exclude: True
tags:
  - boucle
  - string
  - a_trou
---
Le codage de César transforme un message en changeant chaque lettre par une autre obtenue par décalage dans l'alphabet de la lettre d'origine. Par exemple, avec un décalage de 3, le `'A'` se transforme en `'D'`, le `'B'` en `'E'`, ..., le `'X'` en `'A'`, le `'Y'` en `'B'` et le `'Z'` en `'C'`. Les autres caractères (`'!'`, `'?'`...) ne sont pas codés.

La fonction `position_lettre` ci-dessous prend en paramètre une chaîne de caractères de longueur 1 `lettre` et renvoie la position de `lettre` dans l'alphabet à partir de celle de la lettre `'A'`. On n'utilisera cette fonction que lorsque `'A' <= lettre <= 'Z'`.

La fonction `nouvelle_lettre` prend un entier `indice`, compris entre 0
inclus et 26 exclu, et renvoie la lettre de l'alphabet correspondant.
Ainsi, `nouvelle_lettre(0)` revoie `'A'` et `nouvelle_lettre(25)`
renvoie `'Z'`.

La fonction `cesar` prend en paramètres une chaîne de caractères `message` et un nombre entier `decalage` et renvoie le nouveau message codé avec le codage de César utilisant ce `decalage`.

!!! example "Exemples"

    ```pycon
    >>> position_lettre('A')
    0
    >>> position_lettre('B')
    1
    >>> position_lettre('D')
    3
    >>> position_lettre('Z')
    25
    ```
    ```pycon
    >>> nouvelle_lettre(0)
    'A'
    >>> nouvelle_lettre(1)
    'B'
    >>> nouvelle_lettre(12)
    'M'
    >>> nouvelle_lettre(25)
    'Z'
    ```
    ```pycon
    >>> cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4)
    'FSRNSYV E XSYW. ZMZI PE QEXMIVI RWM !'
    >>> cesar('GTSOTZW F YTZX. ANAJ QF RFYNJWJ SXN !', -5)
    'BONJOUR A TOUS. VIVE LA MATIERE NSI !'
    ```

{{ IDE('exo') }}

