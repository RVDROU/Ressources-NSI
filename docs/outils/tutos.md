# Les notebook Jupyter
Jupyter Notebook est une application web qui vous permet de stocker des lignes de code Python, les résultats de l’exécution de ces dernières (graphiques, tableaux, etc.) et du texte formaté. Cela peut être comparé à une page web... contenant du code Python ! Un peu comme ce cours, en fin de compte.

## Découvrir le notebook Jupyter
Jupyter Notebook est un outil puissant qui permet aux utilisateurs du langage Python de créer et de partager des documents interactifs contenant du code dynamique et exécutable, des visualisations de contenus, des textes de documentation et des équations. Le terme "notebook" est lié au caractère intrinsèque de l’outil qui permet d’écrire des petits bouts de code exécutable (appelés "cellules"), de les documenter pour expliquer ce qu’ils font et d’afficher les données résultant de leur exécution. Tout cela est stocké dans un document partageable avec d’autres utilisateurs.

C’est donc particulièrement pratique pour prototyper des algorithmes ou tester des bouts de code, afin d’analyser les résultats et éventuellement de les ajouter à votre projet principal. Avec un notebook, pas besoin d’organiser son code en fonction, avec un main, etc. Vous avez juste besoin d’écrire votre code dans les blocs prédéfinis et de l’exécuter, pour "faire tourner du Python".

##  Premiers pas avec Jupyter
Premièrement, ouvrez Jupyter Notebook : cela va ouvrir un nouvel onglet dans votre navigateur Internet appelé Home. Commencez par créer un nouveau notebook en cliquant sur  New  puis  Python 3  :

Cela va normalement encore ouvrir un nouvel onglet dans lequel se trouvent, de haut en bas : le nom de votre notebook (que vous pouvez modifier en cliquant dessus), une barre de menu, une barre d’outils et une cellule vide. Essayez d’écrire dans cette cellule votre première ligne de code et cliquez ensuite sur Run. Dire "Bonjour" serait par exemple un bon début.


Documentez votre notebook
Avant de vraiment plonger dans la programmation, vous devez savoir qu’il existe 4 types de cellules différentes avec Jupyter : code, markdown, row nbconvert et heading.

Lorsque vous cliquez sur une cellule, vous pouvez changer le type simplement en le sélectionnant dans la liste, comme dans l’exemple ci-dessous :

    Code – la cellule de code classique. Celle-ci est réservée pour l’écriture et l’exécution de code Python ! Vous pouvez exécuter votre code en cliquant sur le bouton  Run, comme vu précédemment.

    Heading – ce type est légèrement obsolète. Jusqu’alors, il servait pour définir des titres, mais les Markdown couvrent aujourd’hui cette fonctionnalité. Il est amené à disparaître dans les prochaines versions de Jupyter.

    Raw nbconvert – permet de contrôler le formatage du document lors d’une conversion du notebook dans un autre format. Vous n’allez pas être amené à l’utiliser dans le cadre de ce cours.

    Markdown – cellule de texte qui sert essentiellement à la documentation du notebook, pour y rédiger des commentaires, des titres, des équations, etc. Ce type permet de structurer votre texte en utilisant les balises HTML ou la syntaxe Markdown.

    Que ce soit pour du Markdown ou du code, il suffit d’écrire votre texte/code et de l’exécuter via le bouton  Run  pour voir le résultat.

On pourrait par exemple créer un titre. Pour cela, il suffit d’ajouter un   #  devant votre texte. De façon similaire à ce que l’on peut avoir avec un logiciel de traitement de texte, un seul  #  correspondra à un titre de niveau 1, deux  #  à un titre de niveau 2, etc. (Voir la documentation Markdown)