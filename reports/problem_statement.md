# Problem Statement

## Context
A polling institute seeks to estimate an individual’s **income group** from personal attributes collected in a survey (`einkommen.train`). The dataset contains **30,000** interviews; the **income label is known for 5,000** individuals and **unknown for 25,000**. Some features have **missing values marked “?”**. A **weighting factor** is provided to compensate interview-dependent selection bias. My job is to predict the income group for the 25,000 unlabeled individuals and prepare the data for subsequent regression/correlation analyses.


## Objective
Train a model to predict a person’s income group (two classes: `≤50k` and `>50k`). Deliver:
- **Calibrated probabilities** for the class `>50k`
- **Predicted class labels** for the **25,000 unlabeled** individuals
- A **clean, analysis-ready dataset** suitable for regression and correlation analyses

## Data Summary (from assignment)
Features include (abridged): Age; Employment type; **Weighting factor**; Education level (ordered); Schooling/training period; Marital status; Employment area; Partnership/relationship; Ethnicity; Gender; Capital gains; Capital losses; Weekly working time; Country of birth; and **Income** (target). Missing values are indicated by `"?"`.

## Label Definition (project convention)
We map the target as a binary label:
- `y = 1` → income `>50k` (positive class)
- `y = 0` → income `≤50k` (negative class)
Rows with income `"?"` are unlabeled and are excluded from training/evaluation; they are used only for out-of-sample prediction.

## Learning Task
Use the **5,000 labeled rows** to develop and select a classifier that outputs both a predicted class and a probability for `>50k`. Then apply the final model to the **25,000 unlabeled rows**. Throughout, handle missing values safely, encode categorical variables consistently, and account for possible class imbalance and selection bias (via the provided weighting factor).

## Assignment Checklist (must cover)
1. Load the data into Python and **preprocess** it.  
2. Choose **data transformations/normalizations** and decide how to handle **missing values ("?")**.  
3. Define which **features** the preprocessed data shall contain.  
4. **Train a model** to predict income group and **apply it to the 25,000 unlabeled individuals**.  
5. Identify a **suitable learning method** and implement it in Python.  
6. **Train and evaluate** the model under a single, consistent evaluation protocol.  
7. Provide **short documentation and motivation** for each step.


## Evaluation Protocol (to be detailed later)
- **Primary metric:** Balanced Accuracy (robust to imbalance)  
- **Secondary:** ROC-AUC, PR-AUC, F1 (positive = `>50k`), Brier score (calibration)  
- **Validation:** Stratified 5-fold CV; preprocessing fit **inside each fold**; report metrics with and without sample weights  
- **Thresholding:** Default 0.5 plus a documented threshold sweep; select the final threshold explicitly

