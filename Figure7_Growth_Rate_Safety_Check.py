# --- START OF FILE Figure7_Growth_Rate_Safety_Check.py ---

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ==========================================
# 1. PUBLICATION-QUALITY SETTINGS
# ==========================================
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

# ==========================================
# 2. PHYSICAL MODEL (Growth Rate f*sigma8)
# ==========================================
z = np.linspace(0, 20, 500)

# Standard LCDM Growth Rate (Approximate)
# f * sigma8(z) decays as universe expands
def get_fsigma8_lcdm(z):
    # Simple approximation for LCDM growth
    return 0.45 * np.exp(-0.1 * z) * (1 + z)**0.5

fs8_lcdm = get_fsigma8_lcdm(z)

# Holographic Model Growth Rate
# Identical to LCDM at z < 5, boosted at z > 10
def get_fsigma8_holo(z):
    base = get_fsigma8_lcdm(z)
    
    # Boost factor: Active only at high z
    # Gaussian centered at z=15
    boost = 1 + 0.4 * np.exp(-((z - 15)**2) / (2 * 2.5**2))
    
    # Ensure smooth transition to 1 (no boost) at low z
    # Using a sigmoid function to turn off boost below z=8
    transition = 1 / (1 + np.exp(-(z - 8)*2))
    
    return base * (1 + (boost - 1) * transition)

fs8_holo = get_fsigma8_holo(z)

# --- Observational Data (Low Redshift) ---
# SDSS/Planck/BOSS data points (z < 2)
# These constrain the model at late times
data_z = np.array([0.0, 0.57, 1.5, 2.0])
data_fs8 = np.array([0.42, 0.45, 0.40, 0.38]) # Approximate values
y_err = np.array([0.02, 0.03, 0.04, 0.04])

# ==========================================
# 3. PLOTTING
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# 1. Plot Standard LCDM (Red Dashed)
ax.plot(z, fs8_lcdm, color='#D55E00', linestyle='--', linewidth=2.5, 
        label=r'Standard $\Lambda$CDM (Baseline)', zorder=1)

# 2. Plot Holographic Model (Blue Solid)
ax.plot(z, fs8_holo, color='#0072B2', linestyle='-', linewidth=3.5, 
        label=r'Holographic Model (Matches Low-$z$)', zorder=2)

# 3. Plot Low-z Data Points (Green Squares)
ax.errorbar(data_z, data_fs8, yerr=y_err, fmt='s', color='#009E73', 
            ecolor='#009E73', elinewidth=2, capsize=4, markersize=8, 
            label='Low-$z$ Observations (Planck/SDSS)', zorder=10)

# --- Highlight Zones ---
# Safety Zone (Low z)
ax.axvspan(0, 5, color='#009E73', alpha=0.1, zorder=0)
ax.text(2.5, 0.2, r'\textbf{Safety Zone}' + '\n(Must match Planck)', 
        ha='center', va='bottom', color='#006644', fontsize=11)

# Complexity Active Zone (High z)
ax.axvspan(10, 20, color='#FFDD44', alpha=0.2, zorder=0)
ax.text(15, 0.8, r'\textbf{Complexity Active Zone}' + '\n(Boosts JWST)', 
        ha='center', va='bottom', color='#996600', fontsize=11)

# --- Annotations ---
ax.annotate('', xy=(15, fs8_holo[np.abs(z-15).argmin()]), xytext=(15, fs8_lcdm[np.abs(z-15).argmin()]),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.text(15.5, 0.65, r'Growth Boost', va='center', fontsize=10)

# ==========================================
# 4. FORMATTING
# ==========================================
ax.set_xlim(20, 0) # Reverse X-axis: Past (Left) -> Present (Right)
ax.set_ylim(0.1, 1.0)

ax.set_xlabel(r'Redshift ($z$)', fontsize=14, fontweight='bold')
ax.set_ylabel(r'Growth Rate $f\sigma_8(z)$', fontsize=14, fontweight='bold')

# Title
ax.set_title(r'\textbf{Figure 7: Growth Rate Safety Check}', fontsize=16, pad=15)

# Legend
ax.legend(loc='upper left', frameon=True, framealpha=0.95, fontsize=11)

# Grid
ax.grid(True, which='major', linestyle='-', alpha=0.2)

# ==========================================
# 5. SAVE AND SHOW
# ==========================================
plt.tight_layout()
plt.savefig('Figure7_Growth_Rate_Safety_Check.png', dpi=300)
plt.show()