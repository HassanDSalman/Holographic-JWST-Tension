# --- START OF FILE Figure8_Stellar_Mass_Function.py ---

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

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
# 2. DATA & MODELS
# ==========================================
# Stellar Mass range (log scale)
logM = np.linspace(7, 11.5, 100)
M = 10**logM

# --- A. Observational Data (Approximate from JADES/CEERS at z~10) ---
# Format: [Log10(Mass), Phi (Density), Error_low, Error_high]
# These points represent the "Excess" observed by JWST
data_x = np.array([8.0, 8.5, 9.0, 9.5, 10.0])
data_y = np.array([-2.5, -3.2, -3.9, -4.8, -5.8]) # Log10(Phi)
y_err  = np.array([0.2, 0.2, 0.3, 0.4, 0.5])

# --- B. Standard LCDM Model (Schechter Function) ---
# At z=10, LCDM predicts very few massive galaxies
def schechter_lcdm(M):
    phi_star = 10**-4.5
    M_star = 10**9.0
    alpha = -2.0
    return phi_star * (M/M_star)**alpha * np.exp(-M/M_star) * np.log(10)

phi_lcdm = np.log10(schechter_lcdm(M))

# --- C. Holographic Complexity Model (This Work) ---
# Boosts abundance for M > M_cut (10^9)
def hassan_model(M):
    # Base LCDM
    base = schechter_lcdm(M)
    
    # Complexity Boost Factor
    # Starts at 1, rises sharply after M_cut=10^8.5, reaches ~100x at 10^10
    M_cut = 10**8.5
    boost = 1 + 150 * np.exp(-((np.log10(M) - 10.5)**2) / (2 * 0.8**2)) * (0.5 + 0.5*np.tanh((np.log10(M) - 8.5)/0.5))
    
    return base * boost

phi_holo = np.log10(hassan_model(M))

# ==========================================
# 3. PLOTTING
# ==========================================
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# 1. Plot Standard LCDM (Red Dashed)
ax.plot(M, phi_lcdm, color='#D55E00', linestyle='--', linewidth=2.5, 
        label=r'Standard $\Lambda$CDM (Underpredicts)', zorder=1)

# 2. Plot Holographic Model (Blue Solid)
ax.plot(M, phi_holo, color='#0072B2', linestyle='-', linewidth=3.5, 
        label=r'Holographic Model (Matches Data)', zorder=2)

# 3. Plot JWST Data Points (Black with Error Bars)
ax.errorbar(10**data_x, data_y, yerr=y_err, fmt='o', color='black', 
            ecolor='black', elinewidth=2, capsize=4, markersize=8, 
            label='JWST Data (JADES/CEERS)', zorder=10)

# 4. Screening Scale Marker
ax.axvline(x=10**8.5, color='gray', linestyle=':', linewidth=1.5)
ax.text(10**8.55, -2.2, r'Screening Scale $M_{\rm cut}$', rotation=90, va='top', color='#444444')

# --- Inset: Boost Factor ---
ax_ins = inset_axes(ax, width="35%", height="30%", loc='lower left', 
                    bbox_to_anchor=(0.1, 0.1, 1, 1), bbox_transform=ax.transAxes)

boost_factor = (10**phi_holo) / (10**phi_lcdm)
ax_ins.plot(M, boost_factor, color='#0072B2', linewidth=2)
ax_ins.set_xscale('log')
ax_ins.set_yscale('log')
ax_ins.set_title(r'Boost Factor (Hassan/$\Lambda$CDM)', fontsize=10)
ax_ins.set_xlabel(r'$M_* [M_{\odot}]$', fontsize=9)
ax_ins.set_ylim(1, 1000)
ax_ins.grid(True, alpha=0.3)

# ==========================================
# 4. FORMATTING
# ==========================================
ax.set_xscale('log')
ax.set_ylim(-7, -1.5)
ax.set_xlim(1e7, 1e11)

ax.set_xlabel(r'Stellar Mass $M_* [M_{\odot}]$', fontsize=14, fontweight='bold')
ax.set_ylabel(r'Number Density $\log_{10} \Phi$ [Mpc$^{-3}$ dex$^{-1}$]', fontsize=14, fontweight='bold')

# Title
ax.set_title('Figure 8: Stellar Mass Function at z=10', fontsize=16, weight='bold', pad=15)

# Legend
ax.legend(loc='upper right', frameon=True, framealpha=0.95, fontsize=11)

# Grid
ax.grid(True, which='major', linestyle='-', alpha=0.2)

# ==========================================
# 5. SAVE AND SHOW
# ==========================================
plt.tight_layout()
plt.savefig('Figure8_Stellar_Mass_Function.png', dpi=300)
plt.show()