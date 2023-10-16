#aerodynamic.py

import matplotlib.pyplot as plt
import numpy as np

from constants import rho, e, g
from aircraft import aircraft

def cl_cd(motor_name, m):
    CD_values = []
    CL_values = []
    alpha = []

    for Vt in np.arange(0, 20.01, 0.01):
        k = (1 / 2) * rho * aircraft.S * (Vt ** 2)
        W = m * g
        
        CL = W / k
        CD = ((CL ** 2) / (np.pi * e * aircraft.AR)) + aircraft.CD0
