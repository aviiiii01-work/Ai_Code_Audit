# Week 6 – Day 2  
## Feature Engineering ML Pipeline

---

## Objective
- Engineer domain features
- Select relevant features safely
- Split data correctly
- Apply encoding and scaling **only on training data**
- Generate final datasets for model training

---

## Folder Structure (Clean & Final)

bootcamp_day2/
├── data/
│   ├── raw/
│   │   └── loan_data.csv
│   └── processed/
│       ├── clean.csv
│       ├── features.csv
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── features/
│   ├── feature_engineering.py
│   ├── feature_selector.py
│   └── feature_list.json
│
└── pipelines/
    └── split_and_transform.py

---

## Important Correction
- ❌ `data_pipeline.py` was **removed**
- ✅ Its logic was redundant and overlapped with `feature_selector.py`
- Each script now has **one clear responsibility**

---

## Golden Rule (Most Important)

Any operation that uses `.fit()` **must be applied only on training data**.  
This includes:
- Encoding
- Scaling
- Feature selection  

Violating this rule causes **data leakage**.

---

## Pipeline Breakdown

### 1. Feature Engineering (features/feature_engineering.py)
- Create derived features:
  - Total_Income
  - Income_by_Loan
  - Loan_to_Income
  - EMI
  - Balance_Income
- No encoding
- No scaling
- No learning from data distribution

Why safe before split:
- Pure mathematical transformations
- No dependency on target or data statistics

Output:
- `data/processed/features.csv`

---

### 2. Feature Selection – Mutual Information (features/feature_selector.py)
- Perform train–test split internally
- Use **only training data**
- Temporarily encode categorical columns
- Compute Mutual Information
- Save selected feature names

Important:
- Encoders here are **temporary**
- Encoded values are **never reused**

Why no leakage:
- Test data and test labels are never seen

Output:
- `features/feature_list.json`

---

### 3. Split, Encode, and Scale (pipelines/split_and_transform.py)
- Load selected feature list
- Split dataset into train and test
- Fit encoders on `X_train`
- Transform `X_train` and `X_test`
- Fit scaler on `X_train`
- Transform `X_train` and `X_test`

Why this is correct:
- Test data is treated as unseen future data
- No statistics leak from test to train

Outputs:
- `X_train.csv`
- `X_test.csv`
- `y_train.csv`
- `y_test.csv`

---

## Correct Execution Order

python features/feature_engineering.py  
python features/feature_selector.py  
python pipelines/split_and_transform.py  

---

## Common Mistakes Avoided
- Encoding before train–test split
- Scaling on full dataset
- Feature selection using test labels
- Reusing encoders from feature selection
- Inflated accuracy due to leakage

---

## Key Takeaway

If a step **learns from data**, it must respect the **train–test boundary**.  
This pipeline is safe for:
- Cross-validation
- Random Forest
- Optuna hyperparameter tuning
- Production deployment
