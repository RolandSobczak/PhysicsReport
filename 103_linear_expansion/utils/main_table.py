import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Stałe: długości początkowe prętów [mm]
COPPER_LENGTH_MM = 771.4
BRASS_LENGTH_MM = 771.45
STEEL_LENGTH_MM = 773.1

# Wczytaj dane
df = pd.read_csv("measurements.csv")

# Dopasowanie prostych (ΔL = a * T + b)
a_cu, b_cu = np.polyfit(df["copper_temperature"], df["copper_length_diff"], 1)
a_brass, b_brass = np.polyfit(df["brass_temperature"], df["brass_length_diff"], 1)
a_steel, b_steel = np.polyfit(df["steel_temperature"], df["steel_length_diff"], 1)

# Oblicz współczynniki rozszerzalności α
alpha_cu = a_cu / COPPER_LENGTH_MM
alpha_brass = a_brass / BRASS_LENGTH_MM
alpha_steel = a_steel / STEEL_LENGTH_MM

print(f"Copper: a = {a_cu:.6f} mm/°C, α = {alpha_cu:.6e} 1/°C")
print(f"Brass:  a = {a_brass:.6f} mm/°C, α = {alpha_brass:.6e} 1/°C")
print(f"Steel:  a = {a_steel:.6f} mm/°C, α = {alpha_steel:.6e} 1/°C")

# Rysowanie danych i prostych dopasowania
plt.plot(df["copper_temperature"], df["copper_length_diff"], "o", label="Copper data")
plt.plot(
    df["copper_temperature"],
    a_cu * df["copper_temperature"] + b_cu,
    "-",
    label="Copper fit",
)

plt.plot(df["brass_temperature"], df["brass_length_diff"], "o", label="Brass data")
plt.plot(
    df["brass_temperature"],
    a_brass * df["brass_temperature"] + b_brass,
    "-",
    label="Brass fit",
)

plt.plot(df["steel_temperature"], df["steel_length_diff"], "o", label="Steel data")
plt.plot(
    df["steel_temperature"],
    a_steel * df["steel_temperature"] + b_steel,
    "-",
    label="Steel fit",
)

# Tytuł i etykiety osi w języku angielskim
plt.title("Thermal Expansion of Metal Rods")
plt.xlabel("Temperature [°C]")
plt.ylabel("Length Change [mm]")
plt.legend(title="Material")
plt.grid(True)

# Zapis wykresu do plików
plt.savefig("expansion_plot.pdf", bbox_inches="tight", dpi=300)
plt.savefig("expansion_plot.png", bbox_inches="tight", dpi=300)

plt.show()
