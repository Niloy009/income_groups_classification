# Problem Statement

A polling institute aims to estimate whether an individual’s annual income exceeds **50,000 USD** based on personal and demographic characteristics.

The original dataset is provided in a raw format (`einkommen.train`) without headers and with missing values denoted by `"?"`. To make it suitable for analysis, I preprocess the file by assigning descriptive column names, converting it into a CSV, and handling missing values.

The dataset consists of approximately **30,000 individuals**, of which the income group is known for **5,000** individuals and unknown for **25,000** individuals. Each record includes demographic, educational, and employment-related attributes.

---

## Task

1. **Data Preparation**  
   - Convert the raw `einkommen.train` file into a structured CSV with proper column names.  
   - Handle missing values (denoted as `"?"`).  
   - Apply appropriate transformations and encodings for categorical and numerical features.  
   - Normalize or scale features where necessary.  
   - Perform **Exploratory Data Analysis (EDA)** in the notebook to understand distributions, detect class imbalance, and visualize key variables.  

2. **Model Training**  
   - Train supervised learning models on the labeled subset (5,000 individuals).  
   - Use classification models (baseline: Logistic Regression; advanced: Random Forest / Gradient Boosting).  
   - Evaluate models with appropriate metrics (Accuracy, Precision, Recall, F1-score, ROC-AUC).  

3. **Prediction**  
   - Select the best-performing model.  
   - Predict the income group for the remaining **25,000 unlabeled individuals**.  
   - Save predictions for further regression and correlation analyses.

---

## Learning Problem

- **Type**: Binary Classification  
- **Target Variable**: `income` (`<=50K` = 0, `>50K` = 1)  
- **Input Features**:  
  - **Numerical**: age, fnlwgt (weighting factor), education_num, capital_gain, capital_loss, hours_per_week  
  - **Categorical**: workclass, education, marital_status, occupation, relationship, race, sex, native_country  

---

## Goal

To build a reliable model that classifies individuals into income groups based on demographic and socio-economic variables. The final model should be able to extend predictions to the unlabeled cases and prepare the data for further statistical analyses.
