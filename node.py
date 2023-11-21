import functools
import numpy as np
from petriNetsClasses import PetriNet
@functools.total_ordering
class Node:

    def __init__(self, marking : np.ndarray):
        self.marking : np.ndarray = marking
        self.transitions : dict[int, Node] = {}
        self.parent : Node = None
    
    def __eq__(self, __value: object) -> bool:
        return np.all(self.marking == __value.marking)
    
    def __ge__(self, __value: object) -> bool:
        return np.all(self.marking >= __value.marking)
    
    def __str__(self) -> str:
         return str(self.marking)
    
    def find_all_child(self, PT : PetriNet):
        possible_transition = [(PT.transition(self.marking, t), t) for t in range(PT.Nt) if PT.transition(self.marking, t) is not None]
        for (new_marking, transition) in possible_transition:
                new_node = Node(new_marking)
                self.transitions[transition] = new_node
                new_node.parent = self
    
    def afficher(self):
        print("Les transitions sont :")
        print(self.transitions)
        print("Le marking est :")
        print(self.marking)