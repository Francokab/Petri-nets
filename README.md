# Petri-nets
 Coverability and Extended Petri nets

# How is the data represented
P set of place : int from 0 to n-1
T set of transition : int from 0 to m-1
W represent the number of token that move in a transition
    Wpt matrix n*m int p->t represent the decrement of places during the transition
    Wtp matrix m*n int t->p represent the increment of places during the transition
M0 et M represent the states of the places : array of int of size n
I represent the inhibition of places on transition
    I matrix n*m int, if p>I(p,t) then t can't happen
    negative value are infinite

# TODO:
    X Adapt PetriNet.transition to work with infinte (negative value)
    - Implement Tree with
        - node : Markings (M and M0...)
        - edge : dict = {t -> node}          
    - Implement path finding algo
    - Implement CT construction algo