# Income Groups Classification

This project is part of the course **Intelligent Data Analysis & Machine Learning I**, taught by **Prof. Dr. Tobias Scheffer** at the University of Potsdam in Summer Semester 2025. <br>


**Goal:** Predict an individual’s income group **(≤50k, >50k)** from personal attributes, using the provided dataset (`einkommen.train`). There are **30,000** interviews; income is **known for 5,000** and **unknown for 25,000** (to be predicted). Some features are missing and marked with **"?"**. A **weighting factor** is provided to compensate interview-dependent selection bias.

**Deliverables:** predictions for the 25k unlabeled individuals and a cleaned, **analysis-ready** dataset for regression/correlation analyses.

## Project layout
- `data/raw/` – original data (`einkommen.train`)
- `data/interim/` – split/clean (no encoding)
- `data/processed/` – fully encoded datasets + final predictions
- `notebooks/` – EDA, preprocessing design, CV modeling, predictions
- `reports/` – figures/tables, **problem statement**, **data dictionary**, slides
- `configs/default.yaml` – seeds, CV folds, preprocessing choices, metrics

## Repro plan (high level)
1. Phase 2: EDA and missingness scan (“?”)  
2. Phase 3: Freeze preprocessing (impute/encode/transform)  
3. Phase 4–6: Baselines → stronger models with unified 5-fold CV  
4. Phase 8: Predict the **25,000** unlabeled cases  
5. Phase 9: Export **analysis-ready** dataset (fully numeric, documented)

