from dataclasses import dataclass
import numpy as np

@dataclass
class PetriNet:
    Wpt: np.ndarray
    Wtp: np.ndarray
    M0: np.ndarray

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