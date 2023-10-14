#performance.py

import matplotlib.pyplot as plt
import numpy as np

from constants import rho, e
from aircraft import aircraft
from force import calculate_forces

def power_traction_velocity(motor_name, m):
    T_values = []
    Tr_values = []
    Te_values = []
    P_values = []
    Pr_values = []
    Pe_values = []
    Vt_values = []
    x = 0

    for Vt in np.arange(5, 17, 0.01):
        Fx, Fy, Fz, Tx, Tz, L, D, W, N, Fat = calculate_forces(Vt, x, motor_name, m)

        k = (1 / 2) * rho * aircraft.S * (Vt ** 2)
        CL = W / k
        CD = ((CL ** 2) / (np.pi * e * aircraft.AR)) + aircraft.CD0

        T_values.append(Tx * rho)
        Tr_values.append(CD * k)
        Te_values.append((Tx * rho) - (CD * k))
        P_values.append(Tx * rho * Vt)
        Pr_values.append(CD * k * Vt)
        Pe_values.append((Tx * rho * Vt) - (CD * k * Vt))
        Vt_values.append(Vt)

    plt.figure(figsize=(8, 5))
    plt.plot(Vt_values, T_values, label="Available")
    plt.plot(Vt_values, Tr_values, label="Required")
    plt.plot(Vt_values, Te_values, label="Excess")
    plt.xlabel("Velocity (m)")
    plt.ylabel("Traction (N)")
    plt.title("Velocity vs. Traction")
    plt.legend()

    plt.figure(figsize=(8, 5))
    plt.plot(Vt_values, P_values, label="Available")
    plt.plot(Vt_values, Pr_values, label="Required")
    plt.plot(Vt_values, Pe_values, label="Excess")
    plt.xlabel("Velocity (m)")
    plt.ylabel("Power (W)")
    plt.title("Velocity vs. Power")
    plt.legend()