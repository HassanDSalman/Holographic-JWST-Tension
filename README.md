# Holographic Complexity and the JWST Tension

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18527237.svg)](https://doi.org/10.5281/zenodo.18527237)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Official Python implementation for: "A Thermodynamic Resolution from Emergent Spacetime"**

This repository contains the numerical scripts used to generate the figures for the research paper addressing the "JWST Tension" via holographic complexity growth.

---

## 📂 Repository Contents

Each script generates a specific figure or validation test from the paper:

| File Name | Description |
| :--- | :--- |
| `Figure1_Collapse_Threshold_Modulation.py` | Visualizes the reduction in critical density threshold (δc). |
| `Figure2_Scale_Dependent_Bias.py` | Shows the unique scale-dependent galaxy bias signature. |
| `Figure4_Dynamic_Collapse_Simulation.py` | Compares halo radius evolution (ΛCDM vs Holographic). |
| `Figure5_Sensitivity_Analysis.py` | Maps the allowed parameter space for the coupling αc. |
| `Figure6_Mass_Dependent_Screening.py` | Demonstrates the surgical precision across mass scales. |
| `Figure7_Growth_Rate_Safety_Check.py` | Validates consistency with late-time Planck observations. |
| `Figure8_Stellar_Mass_Function.py` | Comparison with JWST Stellar Mass Function data at z=10. |
| `Figure9_UV_Luminosity_Function.py` | Comparison with JWST UV Luminosity Function data at z=12. |
| `Figure10_21cm_Golden_Signature.py` | Predicts the ~150% enhancement in the 21cm power spectrum. |

---

## 🚀 Getting Started

### Requirements

Python 3.7+ with the following libraries:

```bash
pip install numpy matplotlib scipy
```

### Usage

Each script is self-contained. To generate a figure (e.g., the 21cm signature), run:

```bash
python Figure10_21cm_Golden_Signature.py
```

---

## 📊 Key Scientific Results

**JWST Validation:** The model achieves a combined χ²/dof ≈ 0.06 across stellar mass and UV luminosity functions, representing a >10,000× improvement over ΛCDM.

**Surgical Precision:** The complexity effect is active only at z > 10 and naturally shuts off at lower redshifts, preserving the standard σ₈ values.

**Falsifiable Prediction:** A localized ~150% boost in the 21cm power spectrum at k* ~ 1 Mpc⁻¹, detectable by HERA Phase II.

---

## 🎓 Citation

If you use this code or the theoretical framework in your research, please cite the definitive version of the paper:

**APA:**

Salman, H. D. (2026). Holographic Complexity and the JWST Tension: A Thermodynamic Resolution from Emergent Spacetime (Version 1.0). Zenodo. https://doi.org/10.5281/zenodo.18527237

**BibTeX:**

```bibtex
@misc{salman_2026_jwst_final,
  author       = {Hassan Dawood Salman},
  title        = {Holographic Complexity and the JWST Tension: A Thermodynamic Resolution from Emergent Spacetime},
  month        = feb,
  year         = 2026,
  publisher    = {Zenodo},
  version      = {1.0},
  doi          = {10.5281/zenodo.18527237},
  url          = {https://doi.org/10.5281/zenodo.18527237}
}
```

---

## 👤 Contact & Links

**Author:** Hassan Dawood Salman

**ORCID:** [0009-0009-1940-0235](https://orcid.org/0009-0009-1940-0235)

**Email:** hassan.d.salman@gmail.com

**Full Paper (Zenodo):** https://doi.org/10.5281/zenodo.18527237

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

The theoretical concepts and the paper itself are associated with the Creative Commons Attribution 4.0 International License as archived on Zenodo.
