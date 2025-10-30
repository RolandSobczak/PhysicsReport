import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_csv("measurements.csv")

# Plot three materials
plt.plot(df["copper_temperature"], df["copper_length_diff"], label="Copper")
plt.plot(df["brass_temperature"], df["brass_length_diff"], label="Brass")
plt.plot(df["steel_temperature"], df["steel_length_diff"], label="Steel")

# Titles and labels
plt.title("Thermal Expansion of Metal Rods")
plt.xlabel("Temperature [°C]")
plt.ylabel("Length Change [mm]")
plt.legend(title="Material")
plt.grid(True)

# Save the plot
# plt.savefig("expansion_plot.pdf", bbox_inches="tight", dpi=300)
plt.savefig("expansion_plot.png", bbox_inches="tight", dpi=300)

# Display
# plt.show()
