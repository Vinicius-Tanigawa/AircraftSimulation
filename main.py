# main.py

import threading as th
import time as t
import tkinter as tk
import matplotlib.pyplot as plt
import queue

from tkinter import ttk
from performance import power_traction_velocity
from aerodynamic import cl_cd
from motors import motors_data
from constants import tolerance
from simulation import simulate_takeoff
from verification import analytic_verification
from energy import kinetic_energy
from plot import (plot_forces_per_distance, plot_fx_per_distance, 
                  plot_fy_per_distance, plot_fz_per_distance, 
                  plot_acceleration_and_velocity_per_distance, 
                  plot_distance_per_time, plot_acceleration_per_distance,
                  plot_velocity_per_distance)

data_plot = queue.Queue()
data_performance = queue.Queue()
data_aerodynamic = queue.Queue()


def start_simulation():
    selected_motor = motor_combobox.get()

    initial_Vt = 0
    initial_x = 0
    max_mass = 10
    min_mass = 2

    clear_labels()

    running_labels()

    start_time = t.time()


    def run_simulation(start_time, initial_Vt, initial_x, selected_motor, 
                       max_mass, min_mass):
        while abs(max_mass - min_mass) > tolerance:
            m = (min_mass + max_mass) / 2

            (takeoff, Vt, x, Vs, m, a, Fx_values, Fy_values, Fz_values, 
             Tx_values, Tz_values, L_values, D_values, W_values, N_values, 
             Fat_values, x_values, V_values, 
             a_values) = simulate_takeoff(initial_Vt, initial_x, selected_motor, m)

            if takeoff:
                min_mass = m
            else:
                max_mass = m

        Vto = analytic_verification(m, selected_motor)

        K = kinetic_energy(m, Vt)

        elapsed_time = t.time() - start_time

        data_plot.put((Fx_values, Fy_values, Fz_values, Tx_values, D_values, 
                        Fat_values, Tz_values, W_values, N_values, L_values, 
                        x_values, V_values, a_values))
        
        data_performance.put((selected_motor, m))
        data_aerodynamic.put(m)

        update_labels(m, a, Vs, Vt, x, Vto, K, elapsed_time)

        return m

    simulation_thread = th.Thread(target=run_simulation, 
                                  args=(start_time, initial_Vt, initial_x, 
                                        selected_motor, max_mass, min_mass))
    simulation_thread.start()


def display_performance():
    data = data_performance.get()

    power_traction_velocity(data[0], data[1])

    plt.show()


def display_aerodynamic():
    data = data_aerodynamic.get()

    cl_cd(data)

    plt.show()


def display_plots():
    data = data_plot.get()

    plot_forces_per_distance(data[10], data[0], data[1], data[2])
    plot_fx_per_distance(data[10], data[3], data[4], data[5])
    plot_fy_per_distance(data[10], data[1])
    plot_fz_per_distance(data[10], data[6], data[7], data[8], data[9])
    plot_acceleration_and_velocity_per_distance(data[10], data[11], data[12])
    plot_acceleration_per_distance(data[10], data[11])
    plot_velocity_per_distance(data[10], data[12])
    plot_distance_per_time(data[10])

    plt.show()


def clear_labels():
    m_label.config(text="")
    a_label.config(text="")
    Vs_label.config(text="")
    Vt_label.config(text="")
    x_label.config(text="")
    Vto_label.config(text="")
    K_label.config(text="")
    time_label.config(text="")

def running_labels():
    start_button.pack_forget()
    loading_label.config(text="Running simulation... Please wait.")
    root.update_idletasks()


def update_labels(m, a, Vs, Vt, x, Vto, K, elapsed_time):
    start_button.pack()
    m_label.config(text=f"\nMass: {m:.2f} kg")
    a_label.config(text=f"Acceleration: {a:.2f} m/s²")
    Vt_label.config(text=f"Velocity: {Vt:.2f} m/s")
    Vs_label.config(text=f"Stall Velocity: {Vs:.2f} m/s")
    x_label.config(text=f"Distance: {x:.2f} m")
    Vto_label.config(text=f"Takeoff Velocity (analytic): {Vto:.2f} m/s")
    K_label.config(text=f"\nKinetc Energy: {K:.0f} J")
    time_label.config(text=f"\nTime Elapsed: {elapsed_time:.2f} s")
    show_plots_button.pack()
    show_performance_button.pack()
    show_aerodynamic_button.pack()
    loading_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Takeoff Simulation")
    root.minsize(400, 300)
    root.resizable(True, True)

    motor_label = ttk.Label(root, text="Select Motor:")
    motor_label.pack()
    motor_combobox = ttk.Combobox(root, values=list(motors_data.keys()), width=30)
    motor_combobox.pack()

    start_button = ttk.Button(root, text="Start Simulation", command=start_simulation)
    start_button.pack()

    m_label = ttk.Label(root, text="")
    m_label.pack()

    a_label = ttk.Label(root, text="")
    a_label.pack()

    Vs_label = ttk.Label(root, text="")
    Vs_label.pack()

    Vt_label = ttk.Label(root, text="")
    Vt_label.pack()

    x_label = ttk.Label(root, text="")
    x_label.pack()

    loading_label = ttk.Label(root, text="")
    loading_label.pack()

    Vto_label = ttk.Label(root, text="")
    Vto_label.pack()

    K_label = ttk.Label(root, text="")
    K_label.pack()

    time_label = ttk.Label(root, text="")
    time_label.pack()

    show_plots_button = ttk.Button(root, text="Show Plots", command=display_plots)
    show_plots_button.pack_forget()

    show_performance_button = ttk.Button(root, text="Show Performance Plots", command=display_performance)
    show_performance_button.pack_forget()

    show_aerodynamic_button = ttk.Button(root, text="Show Aerodynamic Plots", command=display_aerodynamic)
    show_aerodynamic_button.pack_forget()


    root.mainloop()