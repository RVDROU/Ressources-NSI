# Commentaires

{{ py('exo_corr') }}

1. La première partie à compléter est à la fin `#!py return catalan_mem[n]`, on souhaite la valeur d'indice $n$ de cette liste. Ou bien `#!py n >= len(catalan_mem)` auquel cas on peut répondre directement, sinon, il faut le calculer et l'ajouter à la liste, ce qui se fait à la ligne précédente.
2. `somme_cas` est une somme des cas, initialisée à $0$ à la ligne 6. Il y a $n$ cas à étudier de $(0, n-1)$, $(1, n-2)$, $\cdots$, $(n-2, 1)$, $(n-1, 0)$. La boucle `#!py for i in range(n):` fera bien $n$ tours.
    - au premier tour $i=0$, l'autre élément du couple devra être $n-1$
    - au tour suivant $i=1$, l'autre élément du couple devra être $n-2$
    - de manière générale, l'autre élément du couple devra être $n-1-i$
3. La formule pour le cas en $i$ est donc `#!py nb_arbres_binaires(i) * nb_arbres_binaires(n - 1 - i)`
4. Justifions le commentaire ligne 9 `# Ici, catalan_mem sera de longueur n`
    - Si on est entré dans la structure conditionnelle, c'est que `n < len(catalan_mem)`
    - Mais à l'issue de la boucle `nb_arbres_binaires(n - 1)` a été appelé, et donc `catalan_mem` a déjà été mis à jour de manière récursive, et il est donc de longueur `n`.
    - On peut ainsi compléter la ligne 10 `#!py catalan_mem.append(somme_cas)`.

> Il existe d'autres méthodes de calcul, plus efficaces.
