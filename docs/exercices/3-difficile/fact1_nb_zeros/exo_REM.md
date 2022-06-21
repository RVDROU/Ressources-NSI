# Commentaires

## Version simple

```python
nb_zeros_factorielle = [0]

def nb_zeros(n):
    resultat = 0
    while n % 10 == 0:
        n //= 10
        resultat += 1
    return resultat

factorielle = 1
for n in range(1, 1000):
    factorielle *= n
    suivant = nb_zeros(factorielle)
    nb_zeros_factorielle.append(suivant)
```

Ici, on appelle la fonction `nb_zeros` sur un nombre factoriel qui est **très grand**.

## Version efficace

```python
def nb_facteurs_5(n):
    resultat = 0
    while n % 5 == 0:
        n //= 5
        resultat += 1
    return resultat

nb_zeros_factorielle = [0]

for n in range(1, 1000):
    apport = nb_facteurs_5(n)
    suivant = nb_zeros_factorielle[n-1] + apport
    nb_zeros_factorielle.append(suivant)
```

Cette version ressemble beaucoup à la précédente ; presque la même fonction.

La différence essentielle est qu'ici `nb_facteurs` est appelé avec un nombre **petit** en paramètre.

À méditer. Cette différence subtile est très importante. Ici, on gagne sérieusement en efficacité grâce à la taille réduite du paramètre dont le cout est plus faible à traiter.
