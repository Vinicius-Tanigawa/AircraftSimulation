# simulation.py

import numpy as np

from aircraft import aircraft
from constants import g, rho, runway
from force import calculate_forces
from acceleration import update_acceleration


def simulate_takeoff(Vt, x, motor_name, m):
    Vs = np.sqrt((m * g / (aircraft.CLmax * rho / 2 * aircraft.S)))
    takeoff = False

    Tx_values = []
    Tz_values = []
    L_values = []
    D_values = []
    W_values = []
    N_values = []
    Fx_values = []
    Fy_values = []
    Fz_values = []
    Fat_values = []
    x_values = []
    V_values = []
    a_values = []
    
    while True:
        Fx, Fy, Fz, Tx, Tz, L, D, W, N, Fat = calculate_forces(Vt, x, motor_name, m)
        Vt, x, a = update_acceleration(Vt, x, Fx, motor_name, m)

        Tx_values.append(Tx)
        L_values.append(L)
        D_values.append(D)
        W_values.append(W)
        N_values.append(N)
        Fat_values.append(Fat)
        Fx_values.append(Fx)
        Fy_values.append(Fy)
        Fz_values.append(Fz)
        Tz_values.append(Tz)
        x_values.append(x)
        V_values.append(Vt)
        a_values.append(a)

        if Fz < 0 and Vt > (1.2 * Vs):
            takeoff = True
            break
        elif x > runway:
            break
    
    return (takeoff, Vt, x, Vs, m, a, Fx_values, Fy_values, Fz_values, 
            Tx_values, Tz_values, L_values, D_values, W_values, N_values, 
            Fat_values, x_values, V_values, a_values)