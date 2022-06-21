# Commentaires

{{ py('exo_corr') }}

On travaille par accumulation de lignes à partir de la liste `[[1]]` qui contient la ligne 0 qui ne contient qu'un élément.

On fait faire $n$ tours de boucles pour ajouter les lignes $1$ incluse à $n+1$ exclue.

Pour chaque ligne, le premier, comme le dernier terme sont ajoutés individuellement ; il s'agit de $1$.

Les autres termes sont calculés en suivant la formule donnée. Il faut faire attention aux indices.

- On calcule la ligne $k$, on utilise donc les coefficients de la ligne $k-1$. Ceux aux indices $i-1$ et $i$ ; au premier tour de boucle interne $i=1$, et on ajoute bien les termes d'indice 0 et 1.
