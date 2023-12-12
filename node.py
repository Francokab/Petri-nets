import functools
import numpy as np
from petriNetsClasses import PetriNet

class Node:

    def __init__(self, marking : np.ndarray):
        self.marking : np.ndarray = marking
        self.transitions : dict[int, Node] = {}
        self.parent : Node = None
    
    def __eq__(self, __value: object) -> bool:
        if self.marking.shape != __value.marking.shape:
            return False
        
        for i in range(len(self.marking)):
            
            if self.marking[i] >= 0:  # non inf value
                if self.marking[i] != __value.marking[i]:
                    return False
                
            else:  # inf value
                if __value.marking[i] >= 0:
                    return False
                
        return True
    
    def __ge__(self, __value: object) -> bool:
        if self.marking.shape != __value.marking.shape:
            return False
        
        for i in range(len(self.marking)):
            
            if self.marking[i] >= 0:  # non inf value
                if __value.marking[i] >= 0: #  non inf value
                    if self.marking[i] < __value.marking[i]:
                        return False
                else:  # inf value
                    return False
                
            else:  # inf value
                pass  # inf value is always greater or equal than everything
                
        return True
    
    def __gt__(self, __value: object) -> bool:
        return (self >= __value and not self == __value)
    
    def __le__(self, __value: object) -> bool:
        return (__value >= self)
    
    def __lt__(self, __value: object) -> bool:
        return (__value > self)
    
    def __ne__(self, __value: object) -> bool:
        return (not self == __value)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
         return str(self.marking)
    
    # add all possible transition to the transition dict
    def find_all_child(self, PT : PetriNet): 
        possible_transition = [(PT.transition(self.marking, t), t) for t in range(PT.Nt) if PT.transition(self.marking, t) is not None]
        for (new_marking, transition) in possible_transition:
                new_node = Node(new_marking)
                self.transitions[transition] = new_node
                new_node.parent = self

    # add all transition to the transition dict
    def find_all_child_with_none(self, PT : PetriNet): 
        possible_transition = [(PT.transition(self.marking, t), t) for t in range(PT.Nt)]
        for (new_marking, transition) in possible_transition:
                new_node = Node(new_marking)
                self.transitions[transition] = new_node
                new_node.parent = self
    
    def afficher(self):
        print("Les transitions sont :")
        print(self.transitions)
        print("Le marking est :")
        print(self.marking)