

### Communication des acacias 


!!! info "Mécanisme de synchronicité"
    Une des observations les plus anciennes a été faite sur les girafes par Wouter Van Hoven. Il a étudié pendant 2 ans le comportement des girafes dans un parc national en Afrique du Sud. Les girafes ingurgitent environ 80 kg de feuilles par jour. Pourtant, lorsqu'elles arrivent sur un acacia, elles ne restent que quelques minutes, broutent que quelques feuilles puis vont vers un autre arbre. L'arbre a réagi à la présence de la girafe en secrétant des tanins. Ce sont des molécules amères et toxiques pour les girafes. Mais en même temps, l'acacia va émettre de l'éthylène, qui est un gaz qui va se déplacer dans l'air et informer les autres arbres qu'un prédateur est là. Que vont faire les autres arbres ? Ils vont augmenter de manière préventive leur teneur en tanin et se préparer à l'arrivée des girafes.

On vous donne une liste de quantités de feuilles que pourrait manger une girafe sur un arbre à un indice donné le long d'une ligne d'acacias. La seule contrainte, c'est que la girafe ne peut pas manger les feuilles sur deux arbres consécutifs, mais souhaite en manger le plus possible. Écrire une fonction qui indique quelle quantité totale la girafe peut ingurgiter.

!!! example "Exemples"

    ```pycon
    >>> feuilles = [4, 25, 20, 8, 17]
    >>> max_manger(feuilles)
    42
    ```
    La girafe peut manger $25+17 = 42$ feuilles au maximum.

    Prendre $4+20+17$ n'en donne que $41$.

    ```pycon
    >>> feuilles = [4, 6, 5, 7, 4]
    >>> max_manger(feuilles)
    13
    ```

    La girafe peut manger $4+5+4=13$ ou bien $6+7=13$ feuilles au maximum.


```python
    --8<-- "./docs/exercices/3-difficile/acacias/exo.py"
```



??? tip "Indice 1"
    Se poser la question : « Combien peut-elle avoir mangé au maximum à la fin ? »
    
    C'est aussi se poser la question : « A-t-elle manger sur le dernier arbre ? »

    En effet, si on veut envisager une récursion, la question se pose... et donc récursivement aussi...

    Il faut donc envisager de savoir combien la girafe a pu manger au maximum en arrivant à un arbre `i` :

    - sans avoir mangé sur le précédent, auquel cas elle pourra manger ici, en `i`
    - en ayant mangé au précédent, auquel cas elle ne pourra manger ici, en `i`

??? tip "Indice 2"
    On utilisera deux variables :
    
    - `maxi_sans_i` : la quantité maximale que la girafe peut manger **sans** pouvoir manger à la position `i`,
    - `maxi_avec_i` : : la quantité maximale que la girafe peut manger **avec** la position `i` dévorée.

??? tip "Indice 3"
    - On gèrera les cas avec peu d'arbres. Aucun arbre ; aucune feuille.
    - On initialisera correctement les variables.
    - On mettra en place avec prudence la récursion qui permet de progresser jusqu'au bout de la file d'arbres.

