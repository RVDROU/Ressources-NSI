# Commentaires

{{ py('exo_corr') }}

Pour un appel de `catalan(n)` deux cas peuvent se produire.

1. `n` est plus petit que la longueur de la liste, alors le résultat est déjà stocké, il suffit de renvoyer `catalan_mem[n]`.
2. `n` est supérieur ou égal à la longueur de la liste. On va alors faire grandir cette liste en utilisant la formule de récurrence, tant que nécessaire. On se retrouve alors dans le cas 1.

## Preuve de la formule

$$C_n = \begin{cases}
1                                & \quad \text{ si } n = 0\\
C_{n-1}×\dfrac{2(2n - 1)}{n + 1}  & \quad \text{ si } n > 0\\
\end{cases}$$

Nous montrons ici une partie seulement de la preuve. La suite sera dans un autre exercice.

Nous partirons du fait (admis) que $C_n = \dfrac{(2n)!}{(n+1)!n!}$ pour $n\geqslant 0$.

- Pour $n = 0$, on a bien $C_0 = \dfrac{0!}{1!0!} = \dfrac11=1$
- Pour $n>0$, on a $C_{n-1} = \dfrac{(2n-2)!}{(n-1)!n!}$, de sorte que
    - $C_{n-1} × \dfrac{(2n)×(2n-1)}{n(n+1)} = \dfrac{(2n)!}{(n+1)!n!} = C_n$
    - $C_{n-1} × \dfrac{2×(2n-1)}{n+1} = C_n$


>Pour la formule : $C_n = \dfrac{(2n)!}{(n+1)!n!}$ pour $n\geqslant 0$.
>
>Un autre exercice sera consacré à cela.
