import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import csv

# -------------------- LOAD DATA --------------------
def load_data():
    data = {}
    with open("weatherr.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            city = row["City"]
            day = int(row["Day"])
            temp = float(row["Temperature"])

            if city not in data:
                data[city] = {"days": [], "temps": []}

            data[city]["days"].append(day)
            data[city]["temps"].append(temp)

    return data

weather_data = load_data()

# -------------------- FUNCTION TO PLOT --------------------
def show_graph():
    city = city_var.get()
    
    days = np.array(weather_data[city]["days"])
    temps = np.array(weather_data[city]["temps"])

    # NumPy Calculations
    avg = np.mean(temps)
    mx = np.max(temps)
    mn = np.min(temps)

    # Show summary
    result_label.config(
        text=f"City: {city}\nAvg: {avg:.2f}°C | Max: {mx}°C | Min: {mn}°C"
    )

    # Plot Matplotlib Graph
    plt.figure(figsize=(5,4))
    plt.plot(days, temps, marker="o")
    plt.title(f"Temperature Trend - {city}")
    plt.xlabel("Day")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.show()

# -------------------- TKINTER UI --------------------
root = tk.Tk()
root.title("Weather Data Visualizer")
root.geometry("400x300")

tk.Label(root, text="Select City", font=("Arial", 12)).pack(pady=10)

city_var = tk.StringVar()
city_dropdown = ttk.Combobox(root, textvariable=city_var, state="readonly")
city_dropdown['values'] = list(weather_data.keys())
city_dropdown.pack(pady=5)

tk.Button(root, text="Show Temperature Graph", command=show_graph).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
