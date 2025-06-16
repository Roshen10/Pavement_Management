import numpy as np
import matplotlib.pyplot as plt

# Calibration parameters
a0 = 0.002  # example values, tune to field data
a1 = 1.0

# Time axis (years after cracking)
t_years = np.linspace(0, 10, 100)
esa_per_year = 1.2  # cumulative ESAs per year after cracking starts (millions)
NEci = esa_per_year * t_years

# Calculate t50
t50 = (50**a1-0.5*a1) / (a0*a1)

def compute_crx(neci):
    z = np.where(neci < t50, 1, -1)
    crx = 50 * (1 - z) + z * (z * a0 * a1 * neci + z * 0.5**a1 + (1 - z) * 50**a1)**1/a1
    return crx

# Evaluate CRX
crx_vals = compute_crx(NEci)

# Plotting
plt.figure(figsize=(8, 5))
plt.scatter(t_years, crx_vals, label='Crack Progression (CRX)')
plt.xlabel('Years Since Crack Initiation')
plt.ylabel('Cracked Area (%)')
plt.title('HDM-IV Crack Progression Model')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
