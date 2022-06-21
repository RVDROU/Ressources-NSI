---
author: Franck Chambon
title: Arbre binaire de recherche
search:
    - exclude: True
tags:
  - arbre
  - boucle
  - récursivité
  - POO
---
On donne une partie de la classe `ABR` pour implémenter les arbres binaires de recherche **sans doublon** : un ensemble fini de nœuds, éventuellement vide, organisés de manière hiérarchique. C'est une arborescence d'éléments comparables.

Un ABR est une structure de nature récursive :

- soit c'est un ABR vide,
- soit il possède un nœud `racine` qui a les attributs :
    - `gauche` : un sous-ABR à gauche
    - `element` : un élément comparable aux autres
    - `droite` : un sous-ABR à droite
    - l'élément de la racine est strictement supérieure à celui du sous-ABR gauche (s'il est non vide)
    - l'élément de la racine est strictement inférieure à celui du sous-ABR droite (s'il est non vide)

Dans l'implémentation suivante :

- `#!py ABR()` initialise un ABR vide.
- Un ABR, **vide ou non**, possède les méthodes dont le nom est explicite :
    - `est_vide(self)` qui renvoie un booléen
    - `insere(self, element)` qui agit sur l'ABR
    - `est_present(self, element)` qui renvoie un booléen
    - `affichage_infixe(self)` qui renvoie une chaine de caractère composée des affichages des éléments et d'un séparateur, suite à un parcours infixe.

On complètera le code suivant :

{{ py_sujet('exo') }}

!!! example "Exemples"

    ```pycon
    >>> nombres = ABR()
    >>> nombres.est_vide()
    True
    >>> for x in [1, 3, 7, 9, 9]: nombres.insere(x)
    >>> not nombres.est_vide()
    False
    >>> nombres.affichage_infixe()
    '|1|3|7|9|'
    >>> nombres.est_present(7)
    True
    >>> nombres.est_present(8)
    False
    ```

    ```pycon
    >>> fruits_ranges = ABR()
    >>> fruits_ranges.est_vide()
    True
    >>> panier = ["kiwi", "pomme", "abricot", "mangue", "poire"]
    >>> for fruit in panier: fruits_ranges.insere(fruit)
    >>> fruits_ranges.est_vide()
    False
    >>> fruits_ranges.affichage_infixe()
    '|abricot|kiwi|mangue|poire|pomme|'
    >>> fruits_ranges.est_present("pomme")
    True
    >>> fruits_ranges.est_present("cerise")
    False
    ```

{{ IDE('exo') }}
