# Holographic Complexity and the JWST Tension

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18527237.svg)](https://doi.org/10.5281/zenodo.18527237)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ⚠️ Author's note (October 2026) / ملاحظة المؤلف

**English.** The `Figure*.py` scripts are schematic illustrations, not outputs of a full simulation: the model curves, the "JWST data" points and the 21cm amplitude were set by hand. The quoted χ²/dof values and the "~150%" 21cm signal should therefore **not** be treated as results. The idea is presented as an **untested proposal**; the derivations of μ(z) and ∂C/∂δ remain open.

A real (but simple) calculation is provided in `halo_abundance_check.py` (Planck 2018, Eisenstein–Hu spectrum, Sheth–Tormen and Press–Schechter). Its output (`halo_abundance_output.txt`) shows:
- Lowering δc by 2–5% raises massive-halo abundance at z = 10–15 by roughly 1.5–6× (up to ~12× in the Press–Schechter upper bound), **not** 10–200×. Reaching 10–100× needs a ≳25% reduction.
- A lower δc leaves σ8 unchanged and slightly **lowers** halo bias (≈3–5%).
- No comparison to JWST data is included.

**العربية.** سكربتات الأشكال `Figure*.py` توضيحية وليست نتائج محاكاة كاملة: المنحنيات و"بيانات JWST" وسعة إشارة 21cm حُدِّدت يدوياً، لذلك لا تُعدّ قيم χ²/dof ولا إشارة "150%" نتائج. الفكرة **اقتراح لم يُختبر**، واشتقاقا μ(z) و∂C/∂δ مفتوحان. الحساب الحقيقي المبسّط في `halo_abundance_check.py` يُظهر أن خفض δc بنسبة 2–5% يرفع وفرة الهالات الضخمة بنحو 1.5–6 أضعاف فقط، وأن σ8 لا يتغير، وأن انحياز الهالات ينقص قليلاً.

---

## Contents

| Path | Description |
| :--- | :--- |
| `halo_abundance_check.py` | Real calculation of halo-abundance boost from a lower δc. |
| `halo_abundance_output.txt` | Output of the script above. |
| `Figure*.py` | Original figure scripts (hand-set curves; illustrative only). |

## Usage

```bash
pip install numpy scipy matplotlib
python halo_abundance_check.py
```

## Citation

Salman, H. D. (2026). Holographic Complexity and the JWST Tension: A Thermodynamic Resolution from Emergent Spacetime. Zenodo. https://doi.org/10.5281/zenodo.18527237

**Author:** Hassan Dawood Salman · ORCID 0009-0009-1940-0235

## License
MIT (see `LICENSE`). The paper is archived on Zenodo under CC BY 4.0.
