from dataclasses import dataclass
from node import Node
import numpy as np

@dataclass
class PetriNet:
    Wpt: np.ndarray
    Wtp: np.ndarray
    M0: np.ndarray

    @property
    def Np(self):
        return self.Wpt.shape[0]
    
    @property
    def Nt(self):
        return self.Wpt.shape[1]
        
    def transition(self, M: np.ndarray, t: int) -> np.ndarray | None:
        Mout = M.copy()
        Np = Mout.shape[0]
        for i in range(Np):
            if Mout[i] >= 0:  # not inf
                if Mout[i] - self.Wpt[i,t] < 0:  # check if transition is not possible
                    return None
                Mout[i] = Mout[i] - self.Wpt[i,t] + self.Wtp[t,i]
            else:  # is inf, stay inf
                pass
        return Mout
    
    def construct_CT(self):
        # Initialize tree
        tree = Node(self.M0)
        
        # Initialize unprocessed
        unprocessed : list[Node] = [tree]
        processed : list[Node] = []
        
        while (unprocessed != []):
            node = unprocessed[0]
            if node not in processed:
                node.find_all_child(self)
                for transition, new_node in node.transitions.items():
                    unprocessed.append(new_node)
                    # if there is a path between M3 -> M1 with M3 < M2
                        # if M3[p] < M2[i] then M2[i] = inf
                unprocessed.remove(node)
                processed.append(node)
        return tree