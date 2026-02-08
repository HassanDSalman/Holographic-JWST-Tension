# --- START OF FILE Figure2_Scale_Dependent_Bias.py ---

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
# Wavenumber k [h/Mpc]
k = np.logspace(-2, 1, 500)

# Standard LCDM Bias (Scale-Independent on large scales)
# For galaxies at z=1, bias is roughly constant at large scales
b_lcdm = 2.0 * np.ones_like(k)
# Add slight scale dependence at very small scales (non-linear) for realism
b_lcdm = b_lcdm * (1 + 0.1 * (k/5)**1.5)

# Holographic Model Bias
# Predicts a "Bump" at k ~ 1 Mpc^-1 due to the complexity screening scale
def get_bias_holo(k):
    base = b_lcdm
    
    # Gaussian bump centered at k=1
    # Amplitude ~ 10% enhancement
    bump = 0.2 * np.exp(-((np.log10(k) - np.log10(1.0))**2) / (2 * 0.3**2))
    
    return base + bump

b_holo = get_bias_holo(k)

# ==========================================
# 3. PLOTTING
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# 1. Plot Standard LCDM (Red Dashed)
ax.plot(k, b_lcdm, color='#D55E00', linestyle='--', linewidth=2.5, 
        label=r'Standard Halo Bias $b(k)$ ($\Lambda$CDM)', zorder=1)

# 2. Plot Holographic Model (Blue Solid)
ax.plot(k, b_holo, color='#0072B2', linestyle='-', linewidth=3.5, 
        label=r'Holographic Complexity Bias $b_{\rm eff}(k)$', zorder=2)

# --- Highlight Feature ---
# Vertical line at k=1
ax.axvline(x=1.0, color='gray', linestyle=':', linewidth=1.5)
ax.text(1.0, 1.85, r'Complexity Scale $k_* \approx 1$ Mpc$^{-1}$', 
        rotation=90, va='bottom', color='#444444', fontsize=10)

# Arrow pointing to the bump
ax.annotate('', xy=(1.0, 2.2), xytext=(0.3, 2.3),
            arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.text(0.15, 2.32, r'\textbf{Signature of Complexity}' + '\n' + r'(~10\% Enhancement)', 
        fontsize=11, color='#0072B2')

# ==========================================
# 4. FORMATTING
# ==========================================
ax.set_xscale('log')
ax.set_xlim(0.01, 10)
ax.set_ylim(1.8, 2.6)

ax.set_xlabel(r'Wavenumber $k$ [Mpc$^{-1}$]', fontsize=14, fontweight='bold')
ax.set_ylabel(r'Galaxy Bias $b(k)$', fontsize=14, fontweight='bold')

# Title
ax.set_title(r'\textbf{Figure 2: Scale-Dependent Galaxy Bias at z=1.0}', fontsize=16, pad=15)

# Legend
ax.legend(loc='lower right', frameon=True, framealpha=0.95, fontsize=11)

# Grid
ax.grid(True, which='major', linestyle='-', alpha=0.2)
ax.grid(True, which='minor', linestyle=':', alpha=0.1)

# ==========================================
# 5. SAVE AND SHOW
# ==========================================
plt.tight_layout()
plt.savefig('Figure2_Scale_Dependent_Bias.png', dpi=300)
plt.show()