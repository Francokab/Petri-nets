from dataclasses import dataclass
import numpy as np

@dataclass
class PetriNet:
    Wpt: np.ndarray
    Wtp: np.ndarray

