#verification.py

import numpy as np

from aircraft import aircraft
from constants import g, rho, runway, mu
from motors import get_motor_thrust

def analytic_verification(m, motor_name):
    Vs = np.sqrt((m * g / (aircraft.CLmax * rho / 2 * aircraft.S)))

    T0 = get_motor_thrust(motor_name, 0)
    T = get_motor_thrust(motor_name, Vs)

    a = (T0 - T) / (Vs ** 2)

    A = (T0 / m) - mu * g

    B = (1 / m) * ((1/2) * rho * aircraft.S * (aircraft.CD0 - (mu * aircraft.CL0)) + a)

    Vto = np.sqrt((A - (A / np.exp(2 * B * runway))) / B)

    return Vto