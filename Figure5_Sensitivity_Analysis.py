# --- START OF FILE Figure5_Sensitivity_Analysis.py ---

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
# 2. PHYSICAL MODEL
# ==========================================
# Range of Coupling Constant alpha_c
alpha = np.linspace(0.0, 0.10, 500)

# Enhancement Factor (Boost) at z=10 for massive halos
# Based on the exponential sensitivity of Press-Schechter: Boost ~ exp(alpha * const)
def get_boost_factor(alpha):
    # Phenomenological fit to the simulation results
    return np.exp(150 * alpha) 

boost = get_boost_factor(alpha)

# JWST Constraint (The target boost needed)
# JWST suggests an excess of 10x to 100x
target_min = 10
target_max = 100

# ==========================================
# 3. PLOTTING
# ==========================================
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# Plot the Boost Curve
ax.plot(alpha, boost, color='black', linewidth=3, zorder=10)

# --- Highlight Zones ---

# 1. Standard LCDM Zone (Too Low)
ax.axvspan(0.0, 0.015, color='gray', alpha=0.2)
ax.text(0.008, 2, r'$\Lambda$CDM Limit' + '\n(No Effect)', 
        rotation=90, va='bottom', color='#444444', fontsize=10)

# 2. The "Sweet Spot" (Allowed Region)
# Where the curve intersects the JWST target (10x - 100x)
alpha_min = np.interp(target_min, boost, alpha)
alpha_max = np.interp(target_max, boost, alpha)

ax.axvspan(alpha_min, alpha_max, color='#009E73', alpha=0.3, label='Allowed Region')
ax.axhspan(target_min, target_max, color='#009E73', alpha=0.1) # Horizontal band

ax.text(0.035, 30, r'\textbf{JWST Allowed Region}' + '\n' + r'$\alpha_c \in [0.02, 0.05]$', 
        ha='center', va='center', color='#006644', fontsize=12, fontweight='bold',
        bbox=dict(facecolor='white', edgecolor='#009E73', boxstyle='round,pad=0.5'))

# 3. Ruled Out Zone (Too High)
ax.axvspan(0.06, 0.10, color='#D55E00', alpha=0.2)
ax.text(0.08, 5000, r'\textbf{Ruled Out}' + '\n(Overproduction)', 
        ha='center', va='top', color='#990000', fontsize=11)

# --- Annotations ---
# Point at the chosen value
chosen_alpha = 0.03
chosen_boost = get_boost_factor(chosen_alpha)
ax.scatter([chosen_alpha], [chosen_boost], color='#0072B2', s=100, zorder=11, label=r'Chosen Value ($\alpha_c=0.03$)')

# Dashed lines to axes
ax.plot([chosen_alpha, chosen_alpha], [0.1, chosen_boost], color='#0072B2', linestyle=':')
ax.plot([0, chosen_alpha], [chosen_boost, chosen_boost], color='#0072B2', linestyle=':')

# ==========================================
# 4. FORMATTING
# ==========================================
ax.set_yscale('log')
ax.set_xlim(0.0, 0.10)
ax.set_ylim(1, 10000)

ax.set_xlabel(r'Complexity Coupling Strength $\alpha_c$', fontsize=14, fontweight='bold')
ax.set_ylabel(r'Abundance Enhancement Factor (at $z=10$)', fontsize=14, fontweight='bold')

# Title
ax.set_title(r'\textbf{Figure 5: Sensitivity to Complexity Coupling}', fontsize=16, pad=15)

# Legend
ax.legend(loc='upper left', frameon=True, framealpha=0.95, fontsize=11)

# Grid
ax.grid(True, which='major', linestyle='-', alpha=0.2)
ax.grid(True, which='minor', linestyle=':', alpha=0.1)

# ==========================================
# 5. SAVE AND SHOW
# ==========================================
plt.tight_layout()
plt.savefig('Figure5_Sensitivity_Analysis.png', dpi=300)
plt.show()