import numpy as np
import pandas as pd

df = pd.read_csv("measurements.csv")

# Copper
a_cu, b_cu = np.polyfit(df["copper_temperature"], df["copper_length_diff"], 1)

# Brass
a_brass, b_brass = np.polyfit(df["brass_temperature"], df["brass_length_diff"], 1)

# Steel
a_steel, b_steel = np.polyfit(df["steel_temperature"], df["steel_length_diff"], 1)

print(f"Copper a = {a_cu:.6f} mm/°C")
print(f"Brass a = {a_brass:.6f} mm/°C")
print(f"Steel a = {a_steel:.6f} mm/°C")
