

### Nombre Factoriel 


La factorielle d'un entier naturel $n$ se note $n!$, c'est le produit des nombres entiers strictement positifs qui sont inférieurs ou égaux à $n$.

$$n! = 1×2×3×4×...×n$$

- $0! = 1$, c'est un produit vide, donc égal à $1$
- $1! = 1$, c'est un produit avec $1$ comme seul facteur.
- $2! = 1×2 = 2$
- $3! = 1×2×3 = 6$
- $4! = 1×2×3×4 = 24$


La factorielle joue un rôle important en algèbre combinatoire parce qu'il y a $n!$ façons différentes de permuter $n$ objets. Elle apparait dans de nombreuses formules en mathématiques, comme la formule du binôme.

!!! example "Nombre de façons de placer 10 personnes à table"
    Par exemple, la factorielle 10 exprime le nombre de combinaisons possibles de placement des 10 convives autour d'une table (on dit la permutation des convives). Le premier convive s'installe sur l'une des 10 places à sa disposition. Chacun de ses 10 placements ouvre 9 nouvelles possibilités pour le deuxième convive, celles-ci 8 pour le troisième, et ainsi de suite.

    Il y a $10! = 3\,628\,800$ façons de placer 10 personnes à table.

On souhaite calculer et mémoriser dans une liste `factorielle_mem` les nombres factoriels. On propose ici une fonction récursive `factorielle` dont voici le principe :

- `factorielle_mem` est initialisé à `[1]` de sorte que $0!$ est égal à `factorielle_mem[0]`
- `factorielle(n)` fait plusieurs actions :
    - Elle remplit, si nécessaire, `factorielle_mem` avec une boucle.
    - Elle renvoie `n!` en utilisant `factorielle_mem[n]` qui sera donc de taille au moins `n + 1` à la fin de l'appel.
    - On utilisera la variable `fact_i` pour $i!$
    - On utilisera la variable `fact_im1` pour $(i-1)!$

!!! info "Formule récursive"
    Pour $i>0$ on a $i! = (i-1)! × i$, comme on peut le constater sur les exemples

    - $5! = 1×2×3×4×5     = 4! × 5$
    - $6! = 1×2×3×4×5×6   = 5! × 6$
    - $7! = 1×2×3×4×5×6×7 = 6! × 7$

Compléter le code :



!!! example "Exemples"

    ```pycon
    >>> factorielle(5)
    120
    >>> factorielle(10)
    3628800
    ```


```python
    --8<-- "./docs/exercices/2-moyen/nb_factoriel/exo.py"
```

