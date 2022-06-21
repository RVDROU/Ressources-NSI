

### Tri par dénombrement 


> Dans cet exercice on s'interdit d'utiliser `max`, `sort` et `sorted`

On souhaite dans cet exercice trier des tableaux de nombres entiers positifs ou nuls. Les *tableaux* seront représentés par des *listes* Python.

Pour ce faire on utilise l'algorithme du **tri par dénombrement**. Ls étapes de cet algorithme sont les suivantes :

* déterminer la valeur maximale dans la tableau *nombres*
* créer une tableau *effectifs* contenant les effectifs dans le tableau initial de tous les entiers entre 0 et le maximum
* créer une nouvelle liste vide
* parcourir le tableau *effectifs* et ajouter autant de fois que nécessaire chaque indice dans la nouvelle liste

Lors de la dernière étape, si l'effectif à l'indice 3 vaut 2, cela signifie que la valeur 3 est présente 2 fois dans le tableau initial : on l'ajoute donc 2 fois dans la nouvelle liste.

!!! example "Exemple"

    On souhaite trier le tableau *nombres* [4, 5, 4, 2] :

    * La valeur maximale est 5
    * Le tableau *effectifs* est :
  
    |indices|0|1|2|3|4|5|
    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|
    |**effectifs**|0|0|**1**|0|2|1|

    Ce tableau comporte bien 6 valeurs
    
    Le 1 à l'indice 2 signifie que le nombre 2 apparaît 1 fois dans le tableau
    
    * On crée une liste vide

    * On parcourt *effectifs* :
        * à l'indice 0 on trouve l'effectif 0 : on ne fait rien
        * à l'indice 1 on trouve l'effectif 0 : on ne fait rien
        * à l'indice 2 on trouve l'effectif 1 : on ajoute 1 fois le nombre 2 dans la liste
        * à l'indice 3 on trouve l'effectif 0 : on ne fait rien
        * à l'indice 4 on trouve l'effectif 2 : on ajoute 2 fois le nombre 4 dans la liste
        * à l'indice 5 on trouve l'effectif 1 : on ajoute 1 fois le nombre 5 dans la liste

Comme on crée une nouvelle liste de nombres triés, on n'oubliera pas de renvoyer celle-ci à la fin du tri.

!!! note "Remarque"

  Il est aussi possible d'écrire les valeurs triées par dessus la liste de départ au lieu de créer une nouvelle liste. **Afin de réussir les tests proposés dans cet exercice on prendra quand-même  soin de renvoyer la liste modifiée**.

Vous devez écrire deux fonctions :

* `maximum` prend en argument une liste de nombres et renvoie la valeur maximale dans celle-ci
* `tri_denombrement` prend en argument une liste de nombres et la trie en appliquant l'algorithme décrit plus haut. Cette fonction renverra une liste contenant les mêmes valeurs triées dans l'ordre croissant

!!! example "Exemples"

    ```pycon
    >>> liste = [4, 5, 4, 2]
    >>> assert tri_denombrement(liste) == [2, 4, 4, 5]
    >>> liste = [5, 4, 3, 2, 1]
    >>> assert tri_denombrement(liste) == [1, 2, 3, 4, 5]
    >>> liste = []
    >>> assert tri_denombrement(liste) == []
    ```


```python
    --8<-- "./docs/exercices/2-moyen/tri_denombrement/exo.py"
```

