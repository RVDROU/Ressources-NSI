---
author: Franck Chambon
title: Arbre binaire
search:
    - exclude: True
tags:
  - arbre
  - boucle
  - récursivité
  - POO
---
> On rappelle qu'il existe parfois des variations dans les définitions des structures arborescentes, et que pendant un exercice, il faut suivre celles données dans l'énoncé.

On peut définir un **arbre binaire** par :

- Soit un arbre binaire vide (souvent appelé _nil_).
- Soit c'est un nœud qui possède une étiquette et **deux** sous-arbres binaires, un à gauche, un à droite, possiblement vides l'un et/ou l'autre.


Les arbres binaires sont ici modélisés dans Python avec un style POO (Programmation Orientée Objet), et on vous demande de compléter la classe `ArbreBinaire` pour disposer des méthodes `taille` et `hauteur`.

> Dans cet exercice, la définition de la hauteur de l'**arbre binaire vide** est 0.

!!! example "Exemple"

    ``` mermaid
    graph TD
        A2{A2} --> A1{A1}
        A2     --> N3{3}
        A1     --> N1{1}
        A1     --> N2{2}
        N3 --> x3( )
        N3 --> y3( )
        N2 --> x2( )
        N2 --> y2( )
        N1 --> x1( )
        N1 --> y1( )
    ```

    Un arbre binaire de hauteur 3 et de taille 5.

{{ IDE('exo') }}
