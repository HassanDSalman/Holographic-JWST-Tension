import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# --- Publication-Quality Settings ---
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
rcParams['font.size'] = 12
rcParams['axes.linewidth'] = 1.5
rcParams['xtick.major.width'] = 1.5
rcParams['ytick.major.width'] = 1.5
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'
rcParams['xtick.top'] = True
rcParams['ytick.right'] = True

# --- Physical Model Parameters ---
k = np.logspace(-1.5, 1.5, 500)
k_star = 1.0
amplitude = 150.0  # Corrected to 150% to match the final paper
width = 0.4

# Models
enhancement_lcdm = np.zeros_like(k)
enhancement_holo = amplitude * np.exp(-((np.log10(k) - np.log10(k_star))**2) / (2 * width**2))
enhancement_astro = 20.0 * np.exp(-((np.log10(k) - np.log10(0.5))**2) / (2 * 0.8**2))

# Sensitivity (HERA Phase II)
sensitivity = 10.0 + 50.0 * (np.log10(k) - np.log10(0.6))**2
sensitivity[sensitivity < 10] = 10

# --- Plotting ---
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# Plot HERA Sensitivity
ax.fill_between(k, sensitivity, 250, color='#DDDDDD', alpha=0.4, zorder=0)
ax.text(0.05, 180, 'HERA Phase II Sensitivity\n(Detectable Region)', 
        color='#666666', fontsize=10, va='top')

# Plot Models
ax.plot(k, enhancement_lcdm, 'k--', linewidth=2, label='Standard $\Lambda$CDM (Baseline)', zorder=1)
ax.plot(k, enhancement_astro, color='#E69F00', linestyle=':', linewidth=2.5, 
        label='Astrophysical Solutions (Pop III)', zorder=2)
ax.plot(k, enhancement_holo, color='#009E73', linewidth=3.5, 
        label='Holographic Model (This Work)', zorder=10)

# Highlight the Peak
ax.scatter([k_star], [amplitude], color='#D55E00', s=50, zorder=11)
ax.annotate('The Golden Signature\n' + r'$\sim 150\%$ Boost at $k_* \approx 1$ Mpc$^{-1}$', 
            xy=(k_star, amplitude), xytext=(2.5, 120),
            arrowprops=dict(arrowstyle='->', color='#D55E00', lw=2),
            fontsize=11, color='#0072B2', fontweight='bold', ha='center')

# Vertical line
ax.axvline(x=k_star, color='#009E73', linestyle='--', alpha=0.5, linewidth=1)
ax.text(k_star, -15, r'$k_* \approx 1$ Mpc$^{-1}$', color='#009E73', ha='center', fontsize=10)

# --- Formatting ---
ax.set_xscale('log')
ax.set_xlim(0.03, 15)
ax.set_ylim(-20, 220) 
ax.set_xlabel(r'Wavenumber $k$ [Mpc$^{-1}$]', fontsize=14, fontweight='bold')
ax.set_ylabel(r'21cm Power Spectrum Enhancement (%)', fontsize=14, fontweight='bold')

ax.set_title('Figure 10: The 21cm Power Spectrum "Golden Signature"', fontsize=16, weight='bold', pad=15)

ax.legend(loc='upper right', frameon=True, framealpha=0.95, fontsize=11)
ax.grid(True, which='major', linestyle='-', alpha=0.2)

plt.tight_layout()
plt.savefig('Figure10_21cm_Golden_Signature.png', dpi=300)
plt.show()
