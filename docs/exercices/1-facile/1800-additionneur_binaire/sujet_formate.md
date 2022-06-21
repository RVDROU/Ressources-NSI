

### Additionneur binaire 


            1 1 0 1 1 0 1 1
```
Écrire une fonction `addition_binaire` qui prends deux listes de bits en
entrée et qui renvoie une liste de bits en sortie, correspondant à
l'addition binaire des deux nombres.

> On n'utilisera ni la fonction `bin` ni les opérateurs `+`, `//` ou `%`.

Une fonction `additionneur` est fournie. Elle prend en entrée trois valeurs
et renvoie deux nombres, le premier étant le chiffre de poids fort de la
somme et le second le chiffre de poids faible. Le premier chiffre peut-être
interprété comme une retenue. Cette fonction simule les circuits
électroniques usuellement présents dans un additionneur binaire. Ces circuits
sont habituellement codés avec des portes logiques correspondant aux
opérateurs `xor` (ou exclusif), `or` (ou), `and` (et) et `nand` (non et)

![](1800-additionneur_binaire/images/Schema_logique_additionneur_complet.gif)

!!! example "Exemples"
    ```pycon
    >>> additionneur(1, 1, 0)
    (1, 0)
    >>> addition_binaire([1, 1, 1], [1, 1, 1])
    [1, 1, 1, 0]
    >>> addition_binaire([1, 0, 1, 0], [1])
    [1, 0, 1, 1]
    >>> addition_binaire([1, 0, 1, 0], [1,  1])
    [1, 1, 0, 1]
    >>> addition_binaire([1, 0, 1, 0], [1, 1, 0])
    [1, 0, 0, 0, 0]
    >>> addition_binaire([1, 0, 1, 0], [0])
    [1, 0, 1, 0]
    >>> addition_binaire([1, 0, 1, 0], [1, 0, 1, 0])
    [1, 0, 1, 0, 0]
    >>> addition_binaire([1, 0, 1, 0], [1, 0, 0, 0, 0])
    [1, 1, 0, 1, 0]
    >>> addition_binaire([1, 0, 1, 0], [1, 1, 1, 1, 1])
    [1, 0, 1, 0, 0, 1]
    >>> addition_binaire([1, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0])
    [1, 1, 0, 1, 1, 0, 1, 1]
    ```


```python
    --8<-- "./docs/exercices/1-facile/1800-additionneur_binaire/exo.py"
```


!!! tip "Aide"
    On peut afficher la liste des retenues pour s'aider dans le
    développement de la fonction.
