#aerodynamic.py

import matplotlib.pyplot as plt
import numpy as np

from constants import rho, e, g
from aircraft import aircraft

def cl_cd(m):
    CD_values = []
    CL_values = []
    Vt_values = []
    alpha_values = []

    for Vt in np.arange(0.01, 20.01, 0.01):
        k = (1 / 2) * rho * aircraft.S * (Vt ** 2)
        W = m * g
        
        CL = W / k

        CD = ((CL ** 2) / (np.pi * e * aircraft.AR)) + aircraft.CD0

        CD_values.append(CD)
        CL_values.append(CL)
        Vt_values.append(Vt)

    plt.figure(figsize=(8, 5))
    plt.plot(Vt_values, CD_values, label="CD")
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("CD")
    plt.title("Velocity vs. CD")
    plt.legend()

    plt.figure(figsize=(8, 5))
    plt.plot(Vt_values, CL_values, label="CL")
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("CL")
    plt.title("Velocity vs. CL")
    plt.legend()

    plt.figure(figsize=(8, 5))
    plt.plot(CD_values, CL_values, label="CD/CL")
    plt.xlabel("CD")
    plt.ylabel("CL")
    plt.title("CD vs. CL")
    plt.legend()