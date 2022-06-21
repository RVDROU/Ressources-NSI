# Commentaires

## Pas la peine d'échanger

Normalement pour échanger 2 valeurs dans un tableau, il faut faire 3
affectations (ou une affectation double `a, b = b, a`). 

Dans notre cas, puisqu'on sait que le tableau ne contient que des 0 ou des 1, dans le `else` on sait qu'il s'agit d'un 1. On peut doc se passer de l'échange et faire uniquement deux affectations :
```python
        ...
        else:
            zeros_et_uns[debut] = zeros_et_uns[fin]
            zeros_et_uns[fin] = 1
        ...
```
au lieu de :
```python
        ...
        else:
            valeur = zeros_et_uns[debut]
            zeros_et_uns[debut] = zeros_et_uns[fin]
            zeros_et_uns[fin] = valeur
        ...
```

## Compter

On peut compter les 0 et écrire le bon nombre de 0 et de 1 après.
