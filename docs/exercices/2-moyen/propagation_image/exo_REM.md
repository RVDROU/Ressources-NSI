# Commentaires

{{ py('exo_corr') }}

Pour ne rien faire, nous aurions pu insérer `#!py pass` ou un commentaire comme ici.

Nous aurions pu aussi prendre la négation de la condition, et ne pas placer de clause `else`.

Il est plus lisible de traiter les cas faciles explicitement dès le début, plutôt que de retarder un dernier cas simple pour la fin. C'est uniquement un choix esthétique et pédagogique.

En revanche, pour un bloc d'actions court, on préfère

```python
if not condition:
    actions
```

Plutôt que

```python
if condition:
    pass
else:
    actions
```

