# Commentaires

## version itérative

```python
def rendu_monnaie(a_rendre):
    solution = []
    i = 0
    while a_rendre > 0:
        if piece[i] > a_rendre:
            i += 1
        else:
            a_rendre -= piece
            solution.append(piece)
    return solution
```

## Version récursive très discutable...

**Il ne faut pas utiliser de paramètre par défaut mutable !**

```python
def rendu_monnaie(a_rendre, solution=[], i=0):
    if a_rendre == 0:
        return solution
    piece = pieces[i]
    if piece <= a_rendre:
        solution.append(piece)
        return rendu_monnaie(a_rendre - piece, solution, i)
    else :
        return rendu_monnaie(a_rendre, solution, i + 1)
```

## Version récursive avec fonction interne

```python
def rendu_monnaie(a_rendre):
    solution = []

    def rendu_glouton_rec(a_rendre, i):
        "Ajoute à `solution` les pièces à rendre à partir de l'indice `i`"
        if a_rendre == 0:
            return
        piece = pieces[i]
        if piece <= a_rendre:
            solution.append(piece)
            rendu_glouton(a_rendre - piece, i)
        else :
            rendu_glouton(a_rendre, i + 1)

    rendu_glouton_rec(a_rendre, 0)
    return solution
```
