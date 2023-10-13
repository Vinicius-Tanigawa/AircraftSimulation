#acceleration.py

import numpy as np

from force import calculate_forces
from scipy.integrate import odeint
from constants import dt

def update_acceleration(Vt, x, Fx, motor_name, m):
    def equations_of_motion(y, t, motor_name, m):
        Vt, x = y
        Fx = calculate_forces(Vt, x, motor_name, m)[0]

        a = np.array([Fx / m,
                      0.,
                      0.])

        return [a[0], Vt]

    initial_conditions = [Vt, x]
    t_span = [0, dt]

    result = odeint(equations_of_motion, initial_conditions, t_span, args=(motor_name, m))

    Vt, x = result[-1]

    return Vt, x, calculate_forces(Vt, x, motor_name, m)[0] / m