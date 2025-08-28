# Data Dictionary

This document provides descriptions of the variables included in the income dataset (`einkommen.train`).  
The dataset was preprocessed to assign the following column names.

---

| Column Name      | Type        | Description                                                                 |
|------------------|-------------|-----------------------------------------------------------------------------|
| **age**          | Numerical   | Age of the individual (in years).                                           |
| **workclass**    | Categorical | Employment type (e.g., Private, Self-emp, Federal-gov, Local-gov, etc.).    |
| **fnlwgt**       | Numerical   | Weighting factor to adjust for survey selection bias.                       |
| **education**    | Categorical | Highest level of education attained (Bachelors, HS-grad, Masters, etc.).    |
| **education_num**| Numerical   | Years of education completed (numeric representation of `education`).       |
| **marital_status** | Categorical | Marital status (Married, Divorced, Never-married, Widowed, etc.).           |
| **occupation**   | Categorical | Occupation type (Tech-support, Sales, Exec-managerial, Farming, etc.).      |
| **relationship** | Categorical | Family relationship (Husband, Wife, Own-child, Not-in-family, etc.).        |
| **race**         | Categorical | Ethnicity of the individual (White, Black, Asian-Pac-Islander, etc.).       |
| **sex**          | Categorical | Gender of the individual (Male/Female).                                     |
| **capital_gain** | Numerical   | Monetary gains from investments and financial assets.                       |
| **capital_loss** | Numerical   | Monetary losses from investments and financial assets.                      |
| **hours_per_week** | Numerical | Average number of working hours per week.                                   |
| **native_country** | Categorical | Country of birth (e.g., United-States, Germany, India, Mexico, etc.).       |
| **income**       | Target      | Binary target variable: `<=50K` (0) or `>50K` (1).                          |

---

## Notes
- Missing values in categorical columns are denoted by `"?"` in the raw dataset and need to be imputed during preprocessing.  
- The column `education_num` provides a numeric encoding of the `education` level, but both features can be used for analysis.  
- The target variable `income` is only available for **5,000 individuals**; the remaining **25,000 individuals** are unlabeled.
