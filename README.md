# WorkforceLens

**Workforce composition and overtime comparisons | Sanif Mujawar**

Does the observed overtime-attrition gap change when department or tenure composition is held to a common mix? WorkforceLens compares crude rates with directly standardised descriptive rates, rather than making individual predictions.

This is an adaptation of [RetainWise](https://github.com/chasimarshad-bot/RetainWise-Employee-Attrition-Insights). Shared data preparation and code are credited in [provenance](docs/PROVENANCE.md); inherited history remains intact. This repository is a separate analytical version, not evidence of an independently authored original capstone.

## Run

Use Python 3.12. From this repository:

```powershell
py -3.12 -m venv .venv
.venv/Scripts/python.exe -m pip install -r requirements.txt
.venv/Scripts/python.exe -m streamlit run app.py
```

On macOS/Linux, use python3.12 and .venv/bin/python. Reviewed data is included; no credentials are required.

## Analytical focus

The app reports overall attrition, a crude overtime gap, group-specific rates, and a composition-standardised gap. Choose department or tenure band as the stratification field. Both overtime groups receive the same weights: each eligible stratum's share of the pooled eligible population. A stratum is eligible only when both overtime groups contain at least ten records. The app separately reports the crude gap on those same eligible records, so excluded strata are not confused with reweighting effects.

[Method and limitations](docs/METHOD.md) explains the calculation. Standardisation describes an association under chosen weights. It is not causal adjustment, does not establish an overtime effect and leaves other confounders unaddressed. Cells below ten are withheld; this is not an anonymity guarantee.

## Current descriptive results

All 1,470 records meet the common-stratum size rule for both partitions.

| Comparison | Overtime Yes minus No (percentage points) |
|---|---:|
| Crude, all records | 20.09 |
| Common department mix | 20.05 |
| Common tenure-band mix | 19.16 |

The association persists under these two choices of weights. Neither comparison establishes causation or accounts for every relevant difference. Exact rates and coverage are saved in [results.json](docs/results.json). These are calculated findings for Sanif to interpret and review, not a personal reflection attributed to him.

## Source

1,470 fictional records from the IBM HR Analytics practice dataset published by Pavan Subhash on Kaggle. There are no observation dates or verified income currency. Attrition is a dataset proportion, not an annual rate. [Dataset attribution and derivative terms](data/SOURCE.md) remain in force.

## Verification and status

Install requirements-dev.txt and run `python -m pytest -q`. Current-version verification is recorded in [testing](docs/TESTING.md). Original QA reports under inherited/ apply to RetainWise only. The original notebooks and retained descriptive helpers are reusable background evidence, not a new WorkforceLens analysis notebook.

This version has not been deployed. Ch Asim's hosted app is a different project. Sanif's own reflection, assessment-handbook mapping and any independent feedback are not claimed complete.

## Structure

- app.py: new composition-comparison dashboard.
- retainwise/composition.py: standardisation and eligibility rules.
- retainwise/data.py and analysis.py: attributed reused validation and descriptive helpers.
- tests/: current-version tests.
- inherited/: original documentation, scripts and tests for provenance.
- jupyter_notebooks/: inherited executed preparation and descriptive analysis.

The repository is private. No GitHub project board, participant feedback or deployment is claimed for this version.
