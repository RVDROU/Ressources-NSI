# Commentaires

Il s'agit d'un tri original car de complexité linéaire. Avantageux sur ce point, il l'est moins sur les deux point suivants :

* cet algorithme ne s'applique qu'aux valeurs entières positives ou nulles
* il nécessite de créer un tableau annexe contenant les effectifs ce qui peut consommer de la mémoire (imaginez le tri d'un tableau des deux nombres 0 et 1000 : le tableau *effectifs* contient 1001 cellules !)

{{ py('exo_corr', 0, '# TESTS') }}

La fonction `maximum` est classique : on initialise le maximum à `0` puis on lit l'ensemble des valeurs.

Pour la fonction `tri_denombrement` :

* on commence par chercher la valeur maximale
* on crée ensuite le tableau `effectifs` contenant `maximum + 1` fois le nombre `0`
* on lit ensuite l'ensemble des valeurs de `nombres` et on incrémente la cellule `effectifs[nb]` correspondante
* on crée une liste vide `nombres_tries`
* on remplit cette liste vide :
    * on parcourt tous les entiers `n` entre `0` et `maxi`
    * pour chacun d'entre eux, on ajoute autant de fois que nécessaire leur valeur dans `nombres_tries`
    * le nombre d'ajout à faire est donné par l'effectif du nombre : `effectif[n]`
  
Comme on a créé une nouvelle liste pour stocker les valeurs triées, on la renvoie à la fin.



*Remarques :*

* Avec Python, il est possible à l'aide de `enumerate` de parcourir une liste en récupérant à chaque itération les couples *(indice, valeur)*. En utilisant cette technique le boucle principale deviendrait :

``` python
for n, eff in enumerate(effectifs):
    for _ in range(eff):
        nombres_tries.append(n)
```

* Une version *en place* du tri va réécrire les valeurs triées directement dans la liste de départ. Pour ce faire, il faut garder trace de l'indice où l'on doit écrire la prochaine valeur :

```python
def tri_denombrement(nombres):
    maxi = maximum(nombres)

    effectifs = [0] * (maxi + 1)

    for nb in nombres:
        effectifs[nb] += 1

    rang = 0
    for n in range(maxi + 1):
        for i in range(effectifs[n]):
            nombres[rang] = n

    return nombres
```

On renvoie la liste `nombres` afin de rester dans le cadre de l'énoncé mais ce n'est ici pas indispensable.

* On utilise ici une version de l'algorithme utilisant un tableau (un liste avec Python) pour stocker les effectifs. 
  Comme mentionné plus haut cette approche est peu efficace dans certains cas en termes d'utilisation de la mémoire. 
  On pourrait de façon plus efficace utiliser un dictionnaire Python. 
  Dans ce cas, il est inutile de rechercher le maximum et le code devient :

``` python
def tri_denombrement_dico(nombres):
    effectifs = {}
    for nb in nombres:
        if nb in effectifs :
            effectifs[nb] += 1
        else :
            effectifs[nb] = 1

    nombres_tries = []
    for n in effectifs:
        for i in range(effectifs[n]):
            nombres_tries.append(n)
    
    return nombres_tries
```

    * En utilisant la méthode `items` des dictionnaire qui renvoie les couples `(clé, valeur)` on pourrait même faire :




