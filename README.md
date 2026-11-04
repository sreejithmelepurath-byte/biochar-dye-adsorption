# Biochar Dye Adsorption Study

**Can waste sugarcane bagasse, turned into biochar and upgraded with a simple acid treatment, pull a synthetic dye out of water?** Two low-cost adsorbents built from farm waste and tested in batch adsorption experiments.

![Materials Chemistry](https://img.shields.io/badge/Materials-Chemistry-2a9d8f)
![Environmental Science](https://img.shields.io/badge/Environmental-Science-264653)
![Python](https://img.shields.io/badge/Python-analysis-3776AB?logo=python&logoColor=white)

📄 **Case study:** [sreejithmelepurath-byte.github.io/MYPORTFOLIO](https://sreejithmelepurath-byte.github.io/MYPORTFOLIO/)

---

## Why it matters

Dyes discharged by the textile, food, pharmaceutical and cosmetic industries are a persistent water-pollution problem, and conventional treatment is expensive. Biosorption with cheap, abundant biomaterials is far more economical, if the material actually works. Sugarcane bagasse is one of the largest agricultural residues worldwide and is usually just discarded.

## Pipeline

```
Sugarcane bagasse ──► Pyrolysis (300 °C, N₂, 2 h) ──► CS biochar
                                                        │
                              0.6 mol/L oxalic acid ◄───┘
                                        │
                                        ▼
                                      OACS ──► Batch adsorption of phenolphthalein
```

| Property | CS biochar | OACS (modified) |
|---|---|---|
| Feedstock | Sugarcane bagasse | CS biochar base |
| Pyrolysis | 300 °C, N₂, 2 h | Same, then post-treated |
| Surface treatment | None | 0.6 mol/L oxalic acid impregnation |
| Purpose | Baseline low-cost adsorbent | Added carboxylic-acid binding sites |

Three variables were tested in triplicate: **initial dye volume**, **adsorbent dosage** and **contact time**. Full protocol in [`docs/method.md`](docs/method.md).

## What the trends show

- **More dye, less efficient:** % removal drops as dye volume rises (fixed number of sites saturate), while uptake per gram increases.
- **More adsorbent, more removal:** the dosage curve marks the smallest dose that still hits a target, which drives scale-up cost.
- **It's fast:** most uptake happens in the first sampling interval, pointing to readily accessible surface sites rather than slow diffusion.
- **The acid bath helps:** OACS outperforms plain CS biochar, consistent with the extra carboxylic-acid binding sites.

## Analysis code

`src/adsorption.py` turns colorimeter readings into results:

- % removal and adsorption capacity *q* (mg/g)
- replicate means and standard deviations per condition
- **Langmuir** and **Freundlich** isotherm fits
- **pseudo-first-order** and **pseudo-second-order** kinetic fits, with R²

```bash
pip install -r requirements.txt
python src/adsorption.py data/experiment_template.csv
pytest -q
```

Log each run in [`data/experiment_template.csv`](data/experiment_template.csv) (column guide in [`data/README.md`](data/README.md)); the script picks up every row that has both absorbance readings.

## Status

The experimental framework and qualitative behaviour are complete. Absorbance readings are being logged into the template; the isotherm and kinetic fits run as soon as enough replicate data is in.

---

By **Sreejith Sreenivasan (Sree)** · B.Sc. Physics research project · [Portfolio](https://sreejithmelepurath-byte.github.io/MYPORTFOLIO/)
