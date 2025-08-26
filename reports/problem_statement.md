# Problem Statement

## Context
A polling institute seeks to estimate an individual’s **income group** from personal attributes collected in a survey (`einkommen.train`). The dataset contains **30,000** interviews; the **income label is known for 5,000** individuals and **unknown for 25,000**. Some features have **missing values marked “?”**. A **weighting factor** is provided to compensate interview-dependent selection bias. My job is to predict the income group for the 25,000 unlabeled individuals and prepare the data for subsequent regression/correlation analyses.

## Objective
Learn a model that predicts a person’s income group  $Y \in \{ \leq 50\text{k}, > 50\text{k} \}$  from attributes $X$ (demographics, education, work, capital gains/losses, hours/week, country, etc.). Deliver **probabilities** $\hat{p}(Y{=} {>}\,50\text{k}\mid X)$ and **class labels** for all unlabeled cases, and produce a **clean, analysis-ready dataset** suitable for regression/correlation studies.

## Learning Task & Notation
- **Labeled set:** \(\mathcal{D}_L=\{(x_i,y_i,w_i)\}_{i=1}^{5000}\)  
- **Unlabeled set:** \(\mathcal{D}_U=\{(x_j,w_j)\}_{j=1}^{25000}\)  
- **Goal:** Learn \(f_\theta:\mathcal{X}\rightarrow\{0,1\}\) (with \(1 \equiv {>}\,50\text{k}\)) and a score \(s_\theta(x)\approx \hat{p}(Y{=}1\mid x)\).  
- **Weights:** Use the **weighting factor** \(w\) for evaluation (and, where supported, training).

## Assignment Checklist (verbatim requirements)
This project will explicitly cover the following exercise items:
1. **Load the data into Python and preprocess it.**  
2. **Choose adequate data transformations/normalizations** and **decide how to handle missing values (“?”)**.  
3. **Design the feature set** the preprocessed data shall contain.  
4. **Train a model to predict income group** and **apply it to the 25,000 unlabeled individuals**.  
5. **Identify a suitable learning method and implement it in Python.**  
6. **Train and evaluate the model** under a unified protocol.  
7. **Provide short documentation and motivation** for each step.

## Constraints & Risks
- Limited labeled data (5k) → careful CV and regularization.  
- Missingness (“?”) → leakage-safe handling required.  
- High-cardinality categoricals (e.g., country, occupation) → rare-category pooling or robust encodings.



