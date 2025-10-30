import numpy as np
import pandas as pd

# --- Wczytanie danych ---
df = pd.read_csv("../measurements/measurements.csv")

# --- Dane początkowe ---
L0 = {
    "copper": 385.0,  # [mm] – wpisz rzeczywiste długości
    "brass": 385.0,
    "steel": 385.0,
}
dL0 = 0.05  # [mm] – przykładowa niepewność pomiaru długości

metals = ["copper", "brass", "steel"]

results = []

for metal in metals:
    T = df[f"{metal}_temperature"].to_numpy()
    dL = df[f"{metal}_length_diff"].to_numpy()

    # --- Regresja liniowa ΔL = a*T + b ---
    coeffs, cov = np.polyfit(T, dL, deg=1, cov=True)
    a, b = coeffs
    sigma_a, sigma_b = np.sqrt(np.diag(cov))

    # --- Współczynnik rozszerzalności i jego błąd ---
    alpha = a / L0[metal]
    d_alpha = alpha * np.sqrt((sigma_a / a) ** 2 + (dL0 / L0[metal]) ** 2)

    results.append((metal, a, sigma_a, alpha, d_alpha))

# --- Wyniki ---
print(
    f"{'Metal':<8} {'a [mm/°C]':>12} {'σ_a [mm/°C]':>15} {'α [1/°C]':>15} {'Δα [1/°C]':>15}"
)
for metal, a, sa, alpha, da in results:
    print(f"{metal:<8} {a:>12.6f} {sa:>15.6f} {alpha:>15.3e} {da:>15.1e}")
