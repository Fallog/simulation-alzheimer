import abc
import numpy as np
from numpy import ndarray


class OneDimeSpace(abc.ABC):
    end: float
    nb_points: int
    step: float
    space: ndarray

    def __init__(self, end: float, nb_points: int):
        self.end = end
        self.nb_points = nb_points

        self.space = np.linspace(0, end, nb_points)
        self.step = float(self.space[1] - self.space[0])

    def map_value_to_index(self, value: float) -> int:
        return int(value / self.step)


# Shallow class for code clarity
class SpatialSpace(OneDimeSpace):
    pass


# Shallow class for code clarity
class TimeSpace(OneDimeSpace):
    pass
