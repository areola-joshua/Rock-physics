# Quantitative Integrative Rock Physics Modeling and Sensitivity-Based Petrophysical Characterization of "JOSH" Field, Offshore, Niger Delta

A comprehensive subsurface characterization framework that bridges high-resolution wireline petrophysics with dynamic elastic rock physics templates (RPT). This project establishes a calibrated, deterministic workflow for lithofacies discrimination, fluid prediction, and data-driven reservoir engineering using multi-attribute elastic crossplot spaces in the Cenozoic Agbada Formation.

## 📌 Project Overview

Traditional interpretation workflows often struggle with acoustic property overlaps in heterolithic, thin-bedded, or complex clastic reservoirs. This project overcomes those limitations by utilizing a dual-scale analysis approach:

1. **Localized Petrophysics:** High-resolution screening of reservoirs **Zone X** and **Zone Y** between **3,959.92 ft and 4,596.08 ft** to evaluate shale volume ($V_{sh}$), multi-fluid saturation ($S_w$), effective/total porosity ($\phi_e$, $\phi_t$), and permeability.
2. **Regional Rock Physics Diagnostics:** Utilizing the **entire 17,399 ft** logging sequence to build robust compaction baselines, stress-transition models, and elastic properties templates ($AI$, $V_p/V_s$, LMR, and NEI).

---

## 🔬 Core Methodologies & Attribute Workflows

The repository includes code and workflows demonstrating how the following dynamic spaces decouple rock matrix rigidity from pore-fluid incompressibility:

* **Acoustic Impedance ($AI$) vs. $V_p/V_s$:** Maps the mechanical compaction vector and separates ductile, clay-rich shales from rigid quartz skeletons. Identifies Class III AVO gas-sand anomalies.
* **Lambda-Mu-Rho ($LMR$) Space:** Explicitly plots fluid incompressibility ($\lambda\rho$) against matrix rigidity ($\mu\rho$) to isolate clean, porous hydrocarbon zones from tight or diagenetically cemented sandstones.
* **Poisson’s Ratio ($\nu$) vs. $AI$:** Captures mechanical burial trends, mapping transitions from shallow, high-porosity muds down to consolidated reservoir formations.
* **Normalized Elastic Impedance ($NEI$) vs. $V_p/V_s$:** Scales far-offset elastic responses to physical dimension constraints, optimizing background caprock and reservoir isolation for simultaneous seismic inversion.

---

## 📊 Key Results Summary

### Localized Petrophysical Metrics (Target Interval: 3,959.92 ft – 4,596.08 ft)

| Parameter | Zone X | Zone Y |
| --- | --- | --- |
| **Top / Bottom Depth (ft)** | 3,959.92 – 4,089.66 | 4,144.50 – 4,596.08 |
| **Gross Thickness (ft)** | 129.7 | 451.6 |
| **Net-to-Gross (NTG)** | **0.997** | **0.935** |
| **Shale Volume ($V_{sh}$ v/v)** | 0.1052 | 0.1684 |
| **Effective Porosity ($\phi_e$ v/v)** | 0.3149 | 0.3002 |
| **Total Porosity ($\phi_t$ v/v)** | 0.3520 | 0.3604 |
| **Water Saturation ($S_w$ %)** | 37.07% | 38.33% |
| **Permeability (mD)** | **1,795 mD** | **1,942 mD** |

---

## 🚀 Real-World Applications

* **Exploration:** Acts as a dependable direct fluid indicator (DFI) to map lateral sand pinch-outs and subtle stratigraphic traps, mitigating commercial exploration risks.
* **Production Engineering:** Isolates high-rigidity matrix limits ($\mu\rho$) to detect highly cemented intervals, optimizing wellbore placement and preventing drilling/borehole stability hazards.
* **Machine Learning (DNN):** The calibrated petro-elastic clusters generated in this project serve as high-confidence, rock-physics-bound training labels for deep learning neural network architectures optimized for automated clastic seismic facies discrimination.
* **Alternative Energy Transition:** The petrophysical frameworks used to screen high-permeability, interconnected pore networks are transferable to evaluating convective pathways in subsurface geothermal systems.

---

## 📂 Repository Structure

```directory
├── data/                  # Well log datasets (LAS/ASCII format)
├── notebooks/             # Jupyter notebooks for petrophysics & RPT crossplots
├── src/                   # Source code modules (LMR, NEI, and AI equations)
├── outputs/               # Saved figures (Crossplots 4, 5, 6, and 7)
└── README.md              # Project documentation

```

---

## 📑 Core Citations & Author Pedigree

If you utilize these workflows or architectural steps in your research, please cite the following foundational works:

* **Areola, J. J.**, Akpan, V., & Akagbosu, P. I. (2025). *Deep Learning Approaches for Facies Prediction in Subsurface Seismic Data*. Society of Petroleum Engineers (SPE) Nigeria Annual International Conference and Exhibition. SPE-228675-MS. [https://doi.org/10.2118/228675-MS](https://doi.org/10.2118/228675-MS)
* Akagbosu, P. I., **Areola, J. J.**, Ofi, A., & Odofin, D. (2024). *Geothermal Energy Assessment in Africa: A Pathway to Renewable Energy*. Society of Petroleum Engineers (SPE) Nigeria Annual International Conference and Exhibition. SPE-221722-MS. [https://doi.org/10.2118/221722-MS](https://doi.org/10.2118/221722-MS)

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
