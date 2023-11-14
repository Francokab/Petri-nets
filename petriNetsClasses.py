from dataclasses import dataclass
import numpy as np

@dataclass
class PetriNet:
    Wpt: np.ndarray
    Wtp: np.ndarray
    M0: np.ndarray

    def transition(self, M: np.ndarray, t: int) -> np.ndarray | None:
        Mout = M - self.Wpt[:,t] + self.Wtp[t,:]
        if np.any(Mout < 0):
            return None
        return Mout