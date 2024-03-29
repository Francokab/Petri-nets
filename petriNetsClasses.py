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
    
    # tir d'une transition depuis un marking, retourne None si ce n'est pas possible
    def transition(self, M: np.ndarray, t: int) -> np.ndarray | None: 
        Mout = M.copy()
        Np = Mout.shape[0]
        for i in range(Np):
            if self.I is not None:
                if self.I[i,t] < 0: #is inf
                    pass
                elif Mout[i] > self.I[i,t]:
                    return None
            
            if Mout[i] >= 0:  # not inf
                if Mout[i] - self.Wpt[i,t] < 0:  # check if transition is not possible
                    return None
                Mout[i] = Mout[i] - self.Wpt[i,t] + self.Wtp[t,i]
            else:  # is inf, stay inf
                pass
        return Mout
    
    # Create Coverability Tree
    def construct_CT(self):
        # Initialize tree
        tree = nodelib.Node(self.M0)
        
        # Initialize unprocessed
        unprocessed : list[nodelib.Node] = [tree]
        processed : list[nodelib.Node] = []
        
        #Breadth first search
        while (unprocessed != []):
            node = unprocessed[0]
            if node not in processed:
                node.find_all_child(self)
                for transition, new_node in node.transitions.items():
                    unprocessed.append(new_node)
                    
                    # if there is a path between parent_node -> node with parent_node < new_node
                    parent_node = node.parent
                    while (parent_node is not None):
                        if (not parent_node < new_node):
                            parent_node = parent_node.parent
                        else:
                            break
                        
                    # then if parent_node[i] < new_node[i] then new_node[i] = inf
                    if parent_node is not None:
                        for i, value in enumerate(new_node.marking):
                            if parent_node.marking[i] < value:
                                new_node.marking[i] = -1
                                
            unprocessed.remove(node)
            processed.append(node)
        return tree
    
    # Create Coverabilty Tree and check if the selected bound is correct
    def construct_CT_with_bounds(self, p, PTI):
        # Initialize tree
        tree = nodelib.Node(self.M0)
        
        # Initialize unprocessed
        unprocessed : list[nodelib.Node] = [tree]
        processed : list[nodelib.Node] = []
        
        while (unprocessed != []):
            node = unprocessed[0]
            if node not in processed:
                node.find_all_child_with_none(self)
                for transition, new_node in list(node.transitions.items()):
                    if new_node.marking is None:
                        # check if the transition is not possible because its a valid inhbition
                        check_inhbition = False
                        if PTI.I[p,transition] < 0:
                            check_inhbition = False
                        else:
                            if node.marking[p] < 0:
                                check_inhbition = True
                            else:
                                check_inhbition = node.marking[p] > PTI.I[p,transition]
                        # check if the transition is not possible because there isn't enough token
                        check_transition = False
                        for q in range(PTI.Np):
                            if(node.marking[q] < PTI.Wpt[q,transition]):
                                check_transition = True
                        # if its not those two then we have an Incorrect Bound
                        if not(check_transition or check_inhbition):
                            print("Incorrect Bound")
                            return None
                        del node.transitions[transition]
                    else:
                        unprocessed.append(new_node)
                        
                        parent_node = node.parent
                        while (parent_node is not None):
                            check_a = new_node >= parent_node
                            check_b = new_node == parent_node
                            if not (check_a and not check_b):
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

    # transform a PTI bounded into a PT
    def PTI_to_PT(self, b_force = 5):
        out_PT = PetriNet(self.Wpt.copy(), self.Wtp.copy(), self.M0.copy(), self.I.copy())
        if(out_PT.I is not None):
            for index_place, ligne_I in enumerate(out_PT.I):
                ligne_non_inf = False
                for index_transition, value in enumerate(ligne_I): # We detect if there is an inhibition
                    if value >= 0:
                        ligne_non_inf = True
                
                if ligne_non_inf:
                    # Add new lines to Wtp, Wpt and M0
                    temp = np.zeros((out_PT.Wtp.shape[0],out_PT.Wtp.shape[1]+1))
                    temp[:,:-1] = out_PT.Wtp
                    out_PT.Wtp = temp

                    temp = np.zeros((out_PT.Wpt.shape[0]+1,out_PT.Wpt.shape[1]))
                    temp[:-1,:] = out_PT.Wpt
                    out_PT.Wpt = temp

                    temp = np.zeros((out_PT.M0.shape[0]+1))
                    temp[:-1] = out_PT.M0
                    out_PT.M0 = temp

                    b = b_force # test
                    print("Debug : place ",index_place, ", b choisi : ", b)
                    out_PT.M0[-1] = b - out_PT.M0[index_place]
                    for index_transition in range(out_PT.Nt):
                        # the new line is filled with W(pb,t) = W(t,p) and W(t,b) = W(p,t)
                        out_PT.Wtp[index_transition,-1] = out_PT.Wpt[index_place, index_transition]
                        out_PT.Wpt[-1,index_transition] = out_PT.Wtp[index_transition, index_place]
                        
                        if out_PT.I[index_place,index_transition] >= 0: # if the inhbition is not inf
                            # W(t,p') = W(p',t) = b - I(p,t)
                            temp_value = b - out_PT.I[index_place,index_transition]
                            out_PT.Wtp[index_transition,-1] = temp_value
                            out_PT.Wpt[-1,index_transition] = temp_value
        out_PT.I = None
        return out_PT
                


        # detect Inhbition ok
        # if there is inhbition.
            # add new line and column ok
            # loop through them and fill them with W(pb,t) = W(t,p) and ...
            # chose a b
            # W(t,p') = W(p',t) = b - I(p,t) if I(p,t) not inf
            # check if no problem inbition