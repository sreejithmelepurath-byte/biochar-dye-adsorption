# Data

`experiment_template.csv` is the logging template for the batch runs. One row per run; repeat rows with `replicate` = 2 and 3 for triplicates, and duplicate the block with `adsorbent` = `CS` for the unmodified biochar.

| Column | Meaning |
|---|---|
| `series` | `dye_volume`, `dosage` or `contact_time` |
| `adsorbent` | `CS` (plain biochar) or `OACS` (oxalic-acid modified) |
| `dye_volume_ml`, `dye_conc_mol_l` | Volume and molarity of the phenolphthalein solution |
| `adsorbent_mg` | Adsorbent dose |
| `contact_time_min` | Shaking time (contact-time series) |
| `wavelength_nm` | Colorimeter wavelength (546 nm, or 670 nm for dosage/time series) |
| `absorbance_initial`, `absorbance_final` | Colorimeter reading before adsorption and of the filtrate after |

Absorbance columns are left blank until the readings are logged.
