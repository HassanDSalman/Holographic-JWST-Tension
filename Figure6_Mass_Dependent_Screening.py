# --- START OF FILE Figure6_Mass_Dependent_Screening.py ---

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
# Halo Mass range
M = np.logspace(7, 13, 500)

# Critical Mass Scale
M_cut = 1e9 

# Collapse Redshift Calculation (Simplified Model)
# In LCDM, massive halos form later (lower z).
# z_collapse ~ 1.686 / sigma(M)
def get_z_collapse_lcdm(M):
    # Approximate relation: Massive halos collapse later
    return 15 - 2.5 * np.log10(M/1e8)

z_col_lcdm = get_z_collapse_lcdm(M)
# Cap at z=0 for very massive halos
z_col_lcdm[z_col_lcdm < 0] = 0

# Holographic Model
# Boosts z_collapse ONLY for M > M_cut
def get_z_collapse_holo(M):
    base = get_z_collapse_lcdm(M)
    
    # Screening function (Step-like transition)
    # Activates smoothly but sharply around M_cut
    screening = 0.5 * (1 + np.tanh((np.log10(M) - np.log10(M_cut)) / 0.5))
    
    # Boost magnitude (adds ~4 to redshift)
    boost = 4.5 * screening
    
    return base + boost

z_col_holo = get_z_collapse_holo(M)

# ==========================================
# 3. PLOTTING
# ==========================================
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# 1. Plot Standard LCDM (Red Dashed)
ax.plot(M, z_col_lcdm, color='#D55E00', linestyle='--', linewidth=2.5, 
        label=r'Standard $\Lambda$CDM (Massive halos form late)', zorder=1)

# 2. Plot Holographic Model (Blue Solid)
ax.plot(M, z_col_holo, color='#0072B2', linestyle='-', linewidth=3.5, 
        label=r'Holographic Model (Massive halos form early)', zorder=2)

# --- Highlight Zones ---
# Dwarf Galaxy Zone (Unaffected)
ax.axvspan(1e7, M_cut, color='#EEEEEE', alpha=0.6, zorder=0)
ax.text(5e7, 2, r'\textbf{Unaffected Zone}' + '\n(Dwarf Galaxies)', 
        color='#666666', fontsize=11, rotation=0)

# Massive Galaxy Zone (Boosted)
ax.axvspan(M_cut, 1e13, color='#FFDD44', alpha=0.15, zorder=0)
ax.text(5e10, 12, r'\textbf{Boosted Zone}' + '\n(JWST Targets)', 
        color='#996600', fontsize=11, ha='center')

# --- Annotations ---
# Vertical Line at M_cut
ax.axvline(x=M_cut, color='black', linestyle=':', linewidth=1.5)
ax.text(M_cut, 16, r'Screening Scale $M_{\rm cut} \sim 10^9 M_{\odot}$', 
        ha='center', va='bottom', fontweight='bold', bbox=dict(facecolor='white', edgecolor='none'))

# Arrow showing the boost
ax.annotate('', xy=(1e11, 11.5), xytext=(1e11, 7.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.text(1.2e11, 9.5, r'Early Formation', va='center', fontsize=10)

# ==========================================
# 4. FORMATTING
# ==========================================
ax.set_xscale('log')
ax.set_xlim(1e7, 1e13)
ax.set_ylim(0, 18)

ax.set_xlabel(r'Halo Mass $M [M_{\odot}]$', fontsize=14, fontweight='bold')
ax.set_ylabel(r'Collapse Redshift $z_{\rm col}$', fontsize=14, fontweight='bold')

# Title
ax.set_title(r'\textbf{Figure 6: Mass-Dependent Screening Mechanism}', fontsize=16, pad=15)

# Legend
ax.legend(loc='lower left', frameon=True, framealpha=0.95, fontsize=11)

# Grid
ax.grid(True, which='major', linestyle='-', alpha=0.2)

# ==========================================
# 5. SAVE AND SHOW
# ==========================================
plt.tight_layout()
plt.savefig('Figure6_Mass_Dependent_Screening.png', dpi=300)
plt.show()