

### Tri pas insertion 


La méthode du tri par insertion repose sur un double parcours de la liste à trier :

- un parcours de gauche à droite en commençant au deuxième élément donne un indice $i$. On a la garantie que la liste jusqu'à l'indice $i$ exclu est triée ;
- on va parcourir de droite à gauche la portion de liste à gauche de $i$ pour y insérer à la bonne place l'élément d'indice $i$

La fonction `tri_insertion` suivante prend en argument un tableau d'`entiers` et trie ce tableau en utilisant la méthode du tri par insertion. Il s'agit d'un tri en place, comme on l'a vu. Compléter cette fonction pour qu'elle réponde à la spécification demandée.


```python
    --8<-- "./docs/exercices/2-moyen/tri_insertion/exo.py"
```

