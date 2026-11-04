# Experimental method

## 1. Adsorbent preparation

**CS biochar (unmodified)**
1. Sugarcane bagasse collected locally, washed and sun-dried for 60 h.
2. Oven-dried at 60 °C for 48 h, then crushed to a powder.
3. Pyrolysed in a tube furnace at 300 °C (5 °C/min heating rate) under nitrogen for 2 h.

**OACS (oxalic-acid modified)**
1. 2 g of CS biochar stirred into 100 mL of 0.6 mol L⁻¹ oxalic acid at 300 rpm for 2 h.
2. Dehydrated at 60 °C for 24 h, then heated to 120 °C for 90 min.
3. Washed and dried.

The acid treatment grafts carboxylic acid groups onto the biochar surface, adding chemically specific binding sites.

## 2. Batch adsorption

- Stock: 0.001 M phenolphthalein in NaOH, diluted to working concentrations.
- Each run: weighed adsorbent + measured dye solution, mechanically shaken, filtered.
- Residual dye in the filtrate read colorimetrically at 546 nm (670 nm for the dosage and contact-time series).
- Every run in triplicate.

| Variable | Levels tested | Held constant |
|---|---|---|
| Initial dye volume | 12, 10, 8, 6, 4 mL | 50 mg adsorbent, 200 rpm |
| Adsorbent dosage | 10, 20, 30, 40, 50 mg | 10 mL of 0.001 M dye, 200 rpm |
| Contact time | sampled every 10 min | 50 mg adsorbent, 10 mL dye |

**Equipment:** hot air oven, muffle furnace, orbital shaker, digital colorimeter.

## 3. Calculations

- % removal = (A₀ − Aₑ) / A₀ × 100
- Capacity q = (C₀ − Cₑ) · V / m (mg/g)
- Isotherms: Langmuir, Freundlich
- Kinetics: pseudo-first-order, pseudo-second-order

All implemented in `src/adsorption.py`.

## References

1. Sokolowska-Gajda, J. Synthetic dyes based on environmental considerations. *Dyes and Pigments*, 1996, 30(1), 1–20.
2. Hsu, T.C. and Chiang, C.S. Activated sludge treatment of dispersed dye factory wastewater. *J. Environ. Sci. Health A*, 1997, 32(7), 1921–1932.
3. Ali, I., Asim, M. and Khan, T.A. Low cost adsorbents for the removal of organic pollutants from wastewater. *J. Environ. Manage.*, 2012, 113, 170–183.
4. Salleh, M.A.M. et al. Cationic and anionic dye adsorption by agricultural solid wastes: a comprehensive review. *Desalination*, 2011, 280(1), 1–13.
5. Crini, G. Non-conventional low-cost adsorbents for dye removal: a review. *Bioresource Technology*, 2006, 97(9), 1061–1085.
6. Adak, A., Bandyopadhyay, M. and Pal, A. Removal of crystal violet dye from wastewater by surfactant-modified alumina. *Sep. Purif. Technol.*, 2005, 44(2), 139–144.
7. Ghani, W.A.W.K. et al. Adsorption of methylene blue on sawdust-derived biochar and its adsorption isotherms. *J. Purity Util. React. Environ.*, 2013, 2(2), 34–50.
8. Hameed, B.H., Mahmoud, D.K. and Ahmad, A.L. Equilibrium modeling and kinetic studies on the adsorption of basic dye by coconut bunch waste. *J. Hazard. Mater.*, 2008, 158, 65–72.
9. Han, X. et al. Removal of methylene blue using porous biochar from KOH-activated peanut shell biochar. *BioResources*, 2015, 10(2), 2836–2849.
10. Namasivayam, C. and Kavitha, D. Removal of Congo Red from wastewater onto activated carbon from coir pith. *Dyes Pigm.*, 2002, 54, 47–58.
