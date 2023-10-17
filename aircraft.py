#aircraft.py

import numpy as np

from constants import rho, e, g
class aircraft:
    S = 0.3
    AR = 4.

    CL = 0.084256485
    CL0 = 0.718
    CLmax = 1.560279137

    CD0 = 0.065868
    CD = (CL ** 2) / (np.pi * e * AR)