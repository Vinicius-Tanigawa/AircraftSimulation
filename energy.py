#energy.py

import numpy as np

from constants import c


def kinetic_energy(m, V):
    gamma = 1 / np.sqrt((1 - ((V ** 2) / (c ** 2))))

    K = (1 / 2) * (m * (V ** 2)) * gamma

    return K