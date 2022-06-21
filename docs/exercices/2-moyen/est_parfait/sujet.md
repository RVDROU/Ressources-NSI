---
author: BNS2022-9.2, puis Franck Chambon
title: La perfection d'un mot
search:
    - exclude: True
tags:
  - a_trou
  - boucle
  - maths
  - string
---
On affecte à chaque lettre de l'alphabet un code selon le tableau ci-dessous :

|`'A'`|`'B'`|`'C'`|`'D'`|`'E'`|`'F'`|`'G'`|`'H'`|`'I'`|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|$1$|$2$|$3$|$4$|$5$|$6$|$7$|$8$|$9$|

|`'J'`|`'K'`|`'L'`|`'M'`|`'N'`|`'O'`|`'P'`|`'Q'`|`'R'`|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|$10$|$11$|$12$|$13$|$14$|$15$|$16$|$17$|$18$|

|`'S'`|`'T'`|`'U'`|`'V'`|`'W'`|`'X'`|`'Y'`|`'Z'`|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|$19$|$20$|$21$|$22$|$23$|$24$|$25$|$26$|


Pour un mot donné (une chaine de caractères non vide uniquement composée de lettres majuscules), on détermine :

- d'une part son code alphabétique concaténé, obtenu par la juxtaposition du texte des codes de chacun de ses caractères, et lu comme un unique entier,
- et d'autre part, son code additionné, qui est la somme des codes de chacun de ses caractères.

On dit que ce mot est « parfait » si le code additionné divise le code concaténé.

!!! tip "Exemples"

    1. Pour le mot `"PAUL"`, les codes sont $16, 1, 21, 12$.
        - Le code concaténé est la chaine `1612112`, soit l'entier $1\,612\,112$.
        - Son code additionné est l'entier $16 + 1 + 21 + 12$ qui donne $50$.
        - $50$ ne divise pas l'entier $1\,612\,112$ ; par conséquent, le mot `"PAUL"` n'est pas parfait.

    2. Pour le mot `"ALAIN"`, les codes sont $1, 12, 1, 9, 14$.
        - Le code concaténé est la chaine `1121914`, soit l'entier $1\,121\,914$.
        - Le code additionné est l'entier $37$, car $1 + 12 + 1 + 9 + 14 = 37$.
        - $37$ divise l'entier $1\,121\,914$ ; par conséquent, le mot `"ALAIN"` est parfait.

!!! tip "Rappel conversion"
    Pour cet exercice on pourra utiliser `str` et `int` comme fonctions de conversion.
    
    D'autre part, on pourra utiliser la fonction `ord` qui renvoie le code ASCII d'un caractère ASCII passé en paramètre.

    ```pycon
    >>> ord('A')
    65
    >>> ord('B')
    66
    ```

    ```pycon
    >>> str(12)
    '12'
    >>> str(12) + str(14)
    '1214'
    >>> int('1214')
    1214
    >>> int('1214') % 10
    4
    ```

Compléter la fonction `est_parfait` ci-dessous qui prend comme argument une chaine de caractères `mot` (en lettres majuscules) et qui renvoie le code alphabétique concaténé, le code additionné de `mot`, ainsi qu'un booléen qui indique si `mot` est parfait ou pas.

{{ py_sujet('exo') }}

!!! example "Exemples"

    ```pycon
    >>> est_parfait("PAUL")
    (50, 1612112, False)
    >>> est_parfait("ALAIN")
    (37, 1121914, True)
    ```

{{ IDE('exo') }}
