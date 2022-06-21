# Commentaires

## Première version

{{ py('exo_corr') }}


## Variante

Une autre possibilité en initialisant la distance minimale à $+\infty$ et en faisant une boucle sur les éléments du tableau et non sur les indices.

D'autre part, comme ce qui nous intéresse ici est de comparer les distances, nous pouvons nous contenter de calculer le carré de la distance euclidienne. Nous éviterons ainsi la manipulation des nombres flottants.

```python
def distance_carree(point_1, point_2):
    """ Calcule et renvoie le carré de la distance euclidienne
    entre deux points. """
    # vous pouvez ajouter des lignes de code ici si besoin
    x1, y1 = point_1
    x2, y2 = point_2
    return ((x1 - x2)**2 + (y1 - y2)**2)

def plus_proche(points, depart):
    """ Renvoie le point du tableau points se trouvant à la plus 
    courte distance du point depart."""
    point_proche = None
    dist_minimale = float('inf')
    for point in points:
        dist_courante = distance_carree(point, depart)
        if dist_courante < dist_minimale:
            point_proche = point
            dist_minimale = dist_courante
    return point_proche
```
