# --- START OF FILE Figure4_Dynamic_Collapse_Simulation.py ---

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ==========================================
# 1. PUBLICATION-QUALITY SETTINGS
# ==========================================
# These settings ensure the plot looks professional for LaTeX/GitHub
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
rcParams['mathtext.fontset'] = 'cm'

# ==========================================
# 2. PHYSICAL MODEL (SPHERICAL COLLAPSE)
# ==========================================
# We model the radius evolution R(z) for a massive halo (M ~ 10^11 M_sun).
# The collapse is governed by the parametric cycloid solution:
# R = A(1 - cos(theta)), t = B(theta - sin(theta))

def get_radius_evolution(z_collapse):
    """
    Generates the normalized radius evolution for a halo collapsing at z_collapse.
    Returns arrays for redshift (z) and normalized radius (R/R_max).
    """
    theta = np.linspace(0, 2 * np.pi, 500)  # Parametric angle from 0 to 2pi
    
    # Time evolution (t proportional to theta - sin(theta))
    t = (theta - np.sin(theta))
    
    # Normalize time so collapse happens at t_collapse corresponding to z_collapse
    # In matter domination, t ~ 1/(1+z)^(3/2)
    t_collapse = 1.0 / (1 + z_collapse)**1.5
    t_scaled = t * (t_collapse / (2 * np.pi))
    
    # Convert time back to redshift: z = (1/t)^(2/3) - 1
    # Avoid division by zero at t=0
    with np.errstate(divide='ignore'):
        z = (1.0 / t_scaled)**(2/3) - 1
    
    # Radius evolution (Normalized to 1 at turnaround)
    R = 0.5 * (1 - np.cos(theta))
    
    return z, R

# Generate data for Standard Model (LCDM) -> Collapses late (z ~ 6.7)
z_lcdm, R_lcdm = get_radius_evolution(z_collapse=6.7)

# Generate data for Holographic Model -> Collapses early (z ~ 11.2)
z_holo, R_holo = get_radius_evolution(z_collapse=11.2)

# ==========================================
# 3. PLOTTING
# ==========================================
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# --- Plot Curves ---
# Standard LCDM (Red Dashed)
ax.plot(z_lcdm, R_lcdm, color='#D55E00', linestyle='--', linewidth=2.5, 
        label=r'Standard $\Lambda$CDM (Collapses at $z \approx 6.7$)', zorder=2)

# Holographic Model (Blue Solid)
ax.plot(z_holo, R_holo, color='#0072B2', linestyle='-', linewidth=3.5, 
        label=r'Holographic Model (Collapses at $z \approx 11.2$)', zorder=3)

# --- Highlight Zones ---
# 1. JWST Observation Window (The "Target" Zone)
ax.axvspan(10, 20, color='#FFDD44', alpha=0.2, zorder=0)
ax.text(15, 0.95, r'\textbf{JWST Observation Window}' + '\n' + r'(Target Zone $z > 10$)', 
        ha='center', va='top', fontsize=10, color='#996600')

# 2. Complexity Active Zone (Visual aid)
ax.axvspan(20, 35, color='#EEEEEE', alpha=0.5, zorder=0)

# --- Annotations ---
# Arrow indicating the shift
ax.annotate('', xy=(11.2, 0), xytext=(6.7, 0),
            arrowprops=dict(arrowstyle='<-', color='black', lw=2))
ax.text(9, 0.05, r'$\Delta z \approx +4.5$', ha='center', fontsize=11, fontweight='bold')

# Mark Turnaround points
ax.scatter([11.2], [0], color='#0072B2', s=50, zorder=4)
ax.scatter([6.7], [0], color='#D55E00', s=50, zorder=4)

# ==========================================
# 4. FORMATTING
# ==========================================
# Invert X-axis because Redshift decreases as time passes (Left=Past, Right=Future)
ax.set_xlim(35, 5)  

ax.set_ylim(0, 1.1)
ax.set_xlabel(r'Redshift ($z$)', fontsize=14, fontweight='bold')
ax.set_ylabel(r'Normalized Halo Radius $R(z) / R_{\rm max}$', fontsize=14, fontweight='bold')

# Title
ax.set_title(r'\textbf{Figure 4: Dynamic Collapse Simulation}', fontsize=16, pad=15)

# Legend
ax.legend(loc='upper left', frameon=True, framealpha=0.95, fontsize=11)

# Grid
ax.grid(True, which='major', linestyle='-', alpha=0.2)

# ==========================================
# 5. SAVE AND SHOW
# ==========================================
plt.tight_layout()
plt.savefig('Figure4_Dynamic_Collapse_Simulation.png', dpi=300)
plt.show()