import numpy as np
from numpy import ndarray
from spatial.oneD.OneDimSpace import TimeSpace
from compartmental.DynamicRate import DynamicRate


class Compartment:
    actual_value: float
    next_value: float
    time_values: ndarray

    def __init__(self, initial_value: float, time_space: TimeSpace):
        self.actual_value = initial_value
        self.next_value = 0
        self.time_values = np.zeros(time_space.nb_points)
        self.time_values[0] = initial_value

    def __add__(self, other) -> float:
        if isinstance(other, (DynamicRate, Compartment)):
            o = other.actual_value
        else:
            o = other
        return self.actual_value + o

    def __mul__(self, other) -> float:
        if isinstance(other, (DynamicRate, Compartment)):
            o = other.actual_value
        else:
            o = other
        return self.actual_value * o

    def __rmul__(self, other) -> float:
        if isinstance(other, (DynamicRate, Compartment)):
            o = other.actual_value
        else:
            o = other
        return self.actual_value * o

    def __pow__(self, power, modulo=None):
        return self.actual_value ** power

    def update_value_for_next_step(self):
        self.actual_value = self.next_value

    def set_next_value(self, next_value: float):
        self.next_value = next_value

    def fill_time_values(self, time_index: int):
        self.time_values[time_index] = self.next_value
