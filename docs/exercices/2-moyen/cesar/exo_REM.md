# Commentaires

{{ py('exo_corr', 0, '# TESTS') }}

## Modulo 26

Lorsqu'on calcule l'indice de la nouvelle lettre, on prend le reste de
la division par 26 pour obtenir une valeur entre 0 inclus et 26 exclu, ce qui garantit
que l'indice correspond bien à une lettre entre `'A'` et `'Z'`. On dit qu'on
fait le calcul modulo 26. Plus généralement pour un texte ou un tableau,
si on veut être sûr que l'indice est valide, on peut rajouter un modulo
`len(texte)` ou `len(tableau)`.

## Pas si sécurisé

Cette méthode de chiffrement n'est pas du tout sécurisée et très facile
à casser en tentant tous les décalages possibles ou en faisant une
analyse des fréquences des lettres. Pour aller au-delà, vous pouvez
regarder du côté du chiffrement affine ou du chiffre de Vigenère.
