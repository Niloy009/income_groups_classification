# Data Dictionary (v1 – to be finalized in Phase 2)

| Name            | Type                | Description                                  | Missing token | Planned handling (Phase 3) |
|-----------------|---------------------|----------------------------------------------|---------------|----------------------------|
| age             | int                 | Age in years                                 | –             | Median impute + NA flag    |
| workclass       | categorical         | Employment type (Private, Self-emp, Gov, …)  | "?"           | Add "Unknown"; rare-pool   |
| fnlwgt          | int (weight)        | Weighting factor (selection bias correction) | –             | Use as sample_weight       |
| education       | ordinal categorical | Highest education level (ordered)            | –             | Ordinal map                |
| education_num   | int                 | Schooling/training period (years)            | –             | Median impute + NA flag    |
| marital_status  | categorical         | Marital status (7 levels)                    | –             | One-hot                    |
| occupation      | categorical         | Employment area (15 levels)                  | "?"           | Add "Unknown"; rare-pool   |
| relationship    | categorical         | Household/relationship role                  | –             | One-hot                    |
| race            | categorical         | Ethnicity (5 levels)                          | –             | One-hot                    |
| sex             | categorical         | Gender (2 levels)                             | –             | One-hot                    |
| capital_gain    | int                 | Gains on financial assets                    | –             | log1p + NA flag            |
| capital_loss    | int                 | Losses on financial assets                   | –             | log1p + NA flag            |
| hours_per_week  | int                 | Weekly working time                          | –             | Winsorize + NA flag        |
| native_country  | categorical         | Country of birth (~42 levels)                | "?"           | Add "Unknown"; rare-pool   |
| income          | target (cat)        | ≤50k / >50k / "?" (unlabeled 25k)           | "?"           | Binary label in train only |

**Notes.**  
- Missing values are **"?"** in the raw file.  
- Education is **ordered** (Preschool … Doctorate).  
- I will publish a final, fully numeric, encoded table in Phase 9.
