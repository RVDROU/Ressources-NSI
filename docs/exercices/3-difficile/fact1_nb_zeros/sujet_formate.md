

### Nombre de zéros de n! (1) 


On rappelle que, pour $n$ un entier naturel, la factorielle de $n$ se note $n!$ et se définit comme le produit des entiers de $1$ à $n$.

- $0! = 1$, comme un produit vide.
- $1! = 1$
- $2! = 1×2 = 2$
- $3! = 1×2×3 = 6$
- $11! = 1×2×3×4×5×6×7×8×9×10×11 = 39916800$
- $42! = 1405006117752879898543142606244511569936384000000000$

On constate que

- $3!$ se termine par aucun zéro.
- $11!$ se termine par 2 zéros.
- $42!$ se termine par 9 zéros.

Construire un **tableau** de longueur 1000, tel que `nb_zeros_factorielle[n]` contient le nombre de zéros dans l'écriture décimale de $n!$, pour $n$ entier inférieur à $1000$.

!!! example "Exemples"

    ```pycon
    >>> nb_zeros_factorielle[3]
    0
    >>> nb_zeros_factorielle[11]
    2
    >>> nb_zeros_factorielle[42]
    9
    >>> len(nb_zeros_factorielle) >= 1000
    True
    ```


```python
    --8<-- "./docs/exercices/3-difficile/fact1_nb_zeros/exo.py"
```


??? tip "Indice 1"
    Pour une version facile, on pourra utiliser une fonction qui renvoie le nombre de zéros d'un entier, on passera en argument la factorielle d'un entier.

    Après avoir réussi. Tenter une version efficace avec l'indice 2.

??? tip "Indice 2"
    Pour une version efficace, on cherchera à calculer l'augmentation du nombre de zéros, d'une factorielle à une autre, en fonction du nouveau facteur.
    Il s'agit du nombre de fois que l'on peut diviser par 5 ce nouveau facteur.
