from dataclasses import dataclass
import node as nodelib
import numpy as np

@dataclass
class PetriNet:
    Wpt: np.ndarray
    Wtp: np.ndarray
    M0: np.ndarray
    I: np.ndarray | None = None

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
        tree = nodelib.Node(self.M0)
        
        # Initialize unprocessed
        unprocessed : list[nodelib.Node] = [tree]
        processed : list[nodelib.Node] = []
        
        while (unprocessed != []):
            node = unprocessed[0]
            if node not in processed:
                node.find_all_child(self)
                for transition, new_node in node.transitions.items():
                    unprocessed.append(new_node)
                    
                    # if there is a path between parent_node -> node with parent_node < new_node
                        # if parent_node[p] < new_node[i] then new_node[i] = inf
                    parent_node = node.parent
                    while (parent_node is not None):
                        if (not parent_node < new_node):
                            parent_node = parent_node.parent
                        else:
                            break
                    
                    if parent_node is not None:
                        for i, value in enumerate(new_node.marking):
                            if parent_node.marking[i] < value:
                                new_node.marking[i] = -1
                                
            unprocessed.remove(node)
            processed.append(node)
        return tree

    def PTI_to_PT(self):
        pass
        # detect Inhbition
        # if there is inhbition.
            # add new line and column
            # loop through them and fill them with W(pb,t) = W(t,p) and ...
            # chose a b
            # W(t',p) = W(p,t') = b - I(p,t) if I(p,t) not inf
            # check if no problem inbition