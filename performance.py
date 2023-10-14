#performance.py

import matplotlib.pyplot as plt
import numpy as np

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

    for Vt in np.arange(0, 17, 0.01):
        Fx, Fy, Fz, Tx, Tz, L, D, W, N, Fat = calculate_forces(Vt, x, motor_name, m)

        T_values.append(Tx)
        Tr_values.append(D)
        Te_values.append(Tx - D)
        P_values.append(Tx * Vt)
        Pr_values.append(D * Vt)
        Pe_values.append((Tx * Vt) - (D * Vt))
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