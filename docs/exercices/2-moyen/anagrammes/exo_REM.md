# Commentaires

{{ IDE('exo_corr') }}

La fonction `supprime_premier` nécessite de distinguer plusieurs cas de figure :

* le caractère lu est différent du caractère cherché : on le recopie
* le caractère lu est égal au caractère cherché et il n'a pas encore été trouvé (`present` toujours à `#!py False`) : on ne le recopie pas mais on indique qu'on l'a trouvé et supprimé (`#!py present = True`)
* le caractère lu est égal au caractère cherché et il a déjà été trouvé/supprimé : on le recopie
* on renvoie pour finir le couple `(present, resultat)`


Pour la fonction `anagrammes` :

* si les deux chaînes sont de longueur 1, on renvoie le résultat de leur comparaison (cas de base de la récursivité)
* sinon, on supprime le premier caractère de `chaine1` dans les deux chaînes
* chacun des appels `supprime_premier(chaine, cible)` renvoie la chaîne réduite mais aussi un booléen indiquant si la `cible` était présente dans la chaîne
* on se demande alors si `cible` était dans `chaine2` (le premier caractère de `chaine1` est nécessairement dans `chaine1`). On teste
donc le booléen renvoyé par `supprime_premier(chaine2, cible)` :
    * si c'est le cas, on appelle la fonction sur ces chaînes "réduites"
    * si ce n'est pas le cas, on renvoie `#!py False` directement