#aerodynamic.py

import matplotlib.pyplot as plt
import numpy as np

from constants import rho, e, g
from aircraft import aircraft

def cl_cd(m):
    CD_values = []
    CL_values = []
    alpha_values = []

    for alpha in np.arange(-20, 20.01, 0.01):
        Vs = np.sqrt((m * g / (aircraft.CLmax * rho / 2 * aircraft.S)))

        k = (1 / 2) * rho * aircraft.S * (Vs ** 2)
        W = m * g
        
        CL = W / k

        CD = ((CL ** 2) / (np.pi * e * aircraft.AR)) + aircraft.CD0

        CD_values.append(CD * alpha)
        CL_values.append(CL* alpha)
        alpha_values.append(alpha)

    plt.figure(figsize=(8, 5))
    plt.plot(alpha_values, CD_values, label="CD")
    plt.xlabel("Alpha (º)")
    plt.ylabel("CD")
    plt.title("Alpha vs. CD")
    plt.legend()

    plt.figure(figsize=(8, 5))
    plt.plot(alpha_values, CL_values, label="CL")
    plt.xlabel("Alpha (º)")
    plt.ylabel("CL")
    plt.title("Alpha vs. CL")
    plt.legend()

    plt.figure(figsize=(8, 5))
    plt.plot(CD_values, CL_values, label="CD/CL")
    plt.xlabel("CD")
    plt.ylabel("CL")
    plt.title("CD vs. CL")
    plt.legend()