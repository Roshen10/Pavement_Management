import numpy as np
import matplotlib.pyplot as plt

a0 = 12.2
a1 = -90.8

snc_values = np.linspace(2.5, 6.0, 50)
ye4_values = [0.5, 1.0, 2.0, 4.0]

def compute_icx(snc, ye4):
    return a0 * np.exp(a1 * (ye4/snc**2))

# Plot ICX vs SNC for different traffic levels
plt.figure(figsize=(8, 5))

for ye4 in ye4_values:
    icx_vals = compute_icx(snc_values, ye4)
    plt.scatter(snc_values, icx_vals, label=f'Traffic = {ye4} M ESALs/year')

plt.title('HDM-IV Crack Initiation Time vs Structural Number')
plt.xlabel('Structural Number (SNC)')
plt.ylabel('Time to Crack Initiation (ICX, years)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
