# motors.py

motors_data = {
    "Scorpion 3008-1220KV | 9x4.7SF": {
        "thrust_curve": [13.1, -0.244, -0.018, -0.000228]
    },
    "Scorpion 3008-1220KV | 7x6E": {
        "thrust_curve": [7.2, -0.0231, -0.00799, -0.000049]
    },
    "Scorpion 3020-890KV | 9x4.7SF": {
        "thrust_curve": [10.9, -0.199, -0.0179, -0.00028]
    },
    "Scorpion 3020-890KV | 12x3.8SF": {
        "thrust_curve": [16.5, -0.579, -0.0231, -0.000316]
    },
    "T-Motor MN801S 150KV | G32x11": {
        "thrust_curve": [62.359, -1.5027, -0.0124, 0.]
    }
}


def get_motor_thrust(motor_name, Vt):
    thrust_data = motors_data.get(motor_name)

    if thrust_data:
        thrust_curve = thrust_data.get("thrust_curve")

        if thrust_curve:
            return thrust_curve[0] + thrust_curve[1] * Vt + thrust_curve[2] * Vt**2 + thrust_curve[3] * Vt**3
        
    return None