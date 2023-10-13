#plot.py

import matplotlib.pyplot as plt


def plot_forces_per_distance(x_values, Fx_values, Fy_values, Fz_values):
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, Fx_values, label="Fx")
    plt.plot(x_values, Fy_values, label="Fy")
    plt.plot(x_values, Fz_values, label="Fz")
    plt.xlabel("Distance (m)")
    plt.ylabel("Forces (N)")
    plt.title("Forces vs. Distance")
    plt.legend()


def plot_fx_per_distance(x_values, Tx_values, D_values, Fat_values):
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, Tx_values, label="T")
    plt.plot(x_values, D_values, label="D")
    plt.plot(x_values, Fat_values, label="Fat")
    plt.xlabel("Distance (m)")
    plt.ylabel("Fx (N)")
    plt.title("Fx vs. Distance")
    plt.legend()


def plot_fy_per_distance(x_values, Fy_values):
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, Fy_values, label="Fy")
    plt.xlabel("Distance (m)")
    plt.ylabel("Fy (N)")
    plt.title("Fy vs. Distance")
    plt.legend()


def plot_fz_per_distance(x_values, Tz_values, W_values, N_values, L_values):
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, Tz_values, label="T")
    plt.plot(x_values, W_values, label="W")
    plt.plot(x_values, N_values, label="N")
    plt.plot(x_values, L_values, label="L")
    plt.xlabel("Distance (m)")
    plt.ylabel("Fz (N)")
    plt.title("Fz vs. Distance")
    plt.legend()


def plot_acceleration_and_velocity_per_distance(x_values, a_values, V_values):
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, a_values, label="Acceleration", color="blue")
    plt.plot(x_values, V_values, label="Velocity", color="red")
    plt.xlabel("Distance (m)")
    plt.ylabel("Acceleration (m/s²) / Velocity (m/s)")
    plt.title("Acceleration and Velocity vs. Distance")
    plt.legend()


def plot_acceleration_per_distance(x_values, a_values):
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, a_values, label="Acceleration", color="blue")
    plt.xlabel("Distance (m)")
    plt.ylabel("Acceleration (m/s²)")
    plt.title("Acceleration vs. Distance")
    plt.legend()


def plot_velocity_per_distance(x_values, V_values):
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, V_values, label="Velocity", color="red")
    plt.xlabel("Distance (m)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Velocity vs. Distance")
    plt.legend()


def plot_distance_per_time(x_values):
    plt.figure(figsize=(8, 5))
    plt.plot(range(len(x_values)), x_values, label="Distance")
    plt.xlabel("Time (10e-4 s)")
    plt.ylabel("Distance (m)")
    plt.title("Distance vs. Time")
    plt.legend()