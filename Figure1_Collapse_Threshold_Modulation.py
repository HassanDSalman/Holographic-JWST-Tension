import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

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
rcParams['mathtext.fontset'] = 'cm'  # Use LaTeX-like fonts for math

# --- Physical Constants and Parameters ---
delta_c_std = 1.686  # Standard spherical collapse threshold
alpha_c = 0.030      # Complexity coupling constant (calibrated)
M_cut = 1e9          # Critical screening mass (Solar Masses)

# Halo Mass Range (Logarithmic)
M_halo = np.logspace(7.5, 12.5, 1000)

# --- Complexity Correction Function ---
def complexity_correction(M, z, alpha_c, M_cut):
    """
    Calculates the reduction factor based on redshift and halo mass.
    """
    # Redshift evolution (Gaussian centered at Cosmic Dawn)
    z_transition = 8.0
    Psi_z = np.exp(-((z - 15.0) / 10.0)**2) 
    
    # Phase Transition (Mass-dependent screening)
    # Using tanh for a smooth but sharp transition
    transition_width = 0.5 
    Psi_M = 0.5 * (1 + np.tanh((np.log10(M) - np.log10(M_cut)) / transition_width))
    
    return Psi_z * Psi_M

# --- Main Plotting ---
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# 1. Plot Standard LCDM Baseline
ax.axhline(y=delta_c_std, color='black', linestyle='--', linewidth=2.5, 
           label=r'Standard $\Lambda$CDM ($\delta_c \approx 1.686$)', zorder=5)

# 2. Plot Holographic Model Curves
redshifts = [10, 15, 20]
colors = ['#0077BB', '#EE3377', '#EE7733'] # High-contrast, colorblind-friendly

for i, z in enumerate(redshifts):
    Psi = complexity_correction(M_halo, z, alpha_c, M_cut)
    delta_c_eff = delta_c_std * (1 - alpha_c * Psi)
    ax.plot(M_halo, delta_c_eff, color=colors[i], linewidth=3, 
            label=f'Holographic Model ($z={z}$)', zorder=10-i)

# 3. Shaded Physical Zones
# Protected Zone (Dwarf Galaxies)
ax.axvspan(1e7, M_cut, color='gray', alpha=0.1, zorder=0)
ax.text(2e8, 1.52, r'\textbf{Protected Zone}' + '\n(Dwarf Galaxies)', 
        ha='center', va='bottom', fontsize=10, color='#444444', style='italic')

# Complexity-Boosted Zone (Massive Galaxies)
ax.axvspan(M_cut, 1e13, color='#FFDD44', alpha=0.15, zorder=0)
ax.text(5e10, 1.52, r'\textbf{Complexity-Boosted Zone}' + '\n(Massive JWST Galaxies)', 
        ha='center', va='bottom', fontsize=10, color='#996600', style='italic')

# 4. Screening Scale Marker
ax.axvline(x=M_cut, color='#444444', linestyle=':', linewidth=1.5)
ax.text(M_cut, 1.695, r' $M_{\rm cut} \sim 10^9 M_{\odot}$', 
        ha='center', va='bottom', fontsize=11, fontweight='bold', 
        bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=2))

# --- Inset Plot: Barrier Reduction Magnitude ---
# Creates a smaller plot inside to show the percentage change
ax_ins = inset_axes(ax, width="35%", height="30%", loc='lower left', 
                    bbox_to_anchor=(0.12, 0.2, 1, 1), bbox_transform=ax.transAxes)

for i, z in enumerate(redshifts):
    Psi = complexity_correction(M_halo, z, alpha_c, M_cut)
    reduction = 100 * (alpha_c * Psi) # Percentage reduction
    ax_ins.plot(M_halo, reduction, color=colors[i], linewidth=2)

ax_ins.set_xscale('log')
ax_ins.set_ylabel(r'$\Delta \delta_c / \delta_c$ (\%)', fontsize=9)
ax_ins.set_xlabel(r'Halo Mass ($M_{\odot}$)', fontsize=9)
ax_ins.set_title(r'Barrier Reduction Magnitude', fontsize=10)
ax_ins.grid(True, alpha=0.3)
ax_ins.tick_params(labelsize=8)
ax_ins.set_ylim(0, 4.5) 

# --- Final Formatting ---
ax.set_xscale('log')
ax.set_xlim(1e8, 2e12)
ax.set_ylim(1.50, 1.72)

ax.set_xlabel(r'Halo Mass $M$ [$M_{\odot}$]', fontsize=14, fontweight='bold')
ax.set_ylabel(r'Critical Collapse Threshold $\delta_{c,\rm eff}$', fontsize=14, fontweight='bold')

# Annotation Arrow
ax.annotate('', xy=(1e11, 1.63), xytext=(1e11, 1.68),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.text(1.1e11, 1.655, r'Easier Collapse' + '\n' + r'(Negative Work)', 
        va='center', fontsize=10)

# Title and Legend
ax.set_title(r'\textbf{Figure 1: Complexity-Modulated Collapse Threshold}', fontsize=16, pad=15)
ax.legend(loc='upper right', frameon=True, framealpha=0.95, fontsize=11)
ax.grid(True, which='major', linestyle='-', alpha=0.2)

# Save and Show
plt.tight_layout()
plt.savefig('Figure1_Collapse_Threshold_Modulation.png', dpi=300)
plt.show()