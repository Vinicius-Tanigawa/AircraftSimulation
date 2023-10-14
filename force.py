# physics.py

import numpy as np
from aircraft import aircraft

from constants import mu, g, rho, runway
from motors import get_motor_thrust


def calculate_forces(Vt, x, motor_name, m, rho=rho, S=aircraft.S, mu=mu):
    if x >= (0.85 * runway):
        alpha = (2 / 5) * ((x - (0.85 * runway)) ** 2)
    else:
        alpha = 0
    
    L = (aircraft.CL0 + (aircraft.CLalpha * alpha)) * ((rho * (Vt ** 2)) / 2) * aircraft.S
    T = np.array([get_motor_thrust(motor_name, Vt) * np.cos(alpha * (np.pi / 180)), 
                  0., 
                  get_motor_thrust(motor_name, Vt) * np.sin(alpha* (np.pi / 180))])
    D = aircraft.CD0 * ((rho * (Vt ** 2)) / 2) * aircraft.S
    W = m * g
    N = max(0, W - L)
    Fat = N * mu

    forces = np.array([T[0] - D - Fat, 
                       0., 
                       W - L - N - T[2]])

    return forces[0], forces[1], forces[2], T[0], T[2], L, D, W, N, Fat