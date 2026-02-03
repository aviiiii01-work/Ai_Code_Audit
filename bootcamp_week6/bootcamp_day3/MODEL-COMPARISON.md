# Model Comparison – Day 3 (Training & Evaluation)

## Objective
The goal of Day-3 was to **train multiple machine learning models**, evaluate them using **cross-validation**, compare their performance using standard metrics, and **automatically select the best performing model** for deployment.

This document summarizes:
- Models used
- Evaluation strategy
- Metrics compared
- Final model selection logic

---

## Models Trained

The following models were trained and evaluated:

### 1. Logistic Regression
- **Type:** Linear model
- **Use case:** Baseline model
- **Strengths:**
  - Fast to train
  - Easy to interpret
  - Works well for linearly separable data
- **Limitations:**
  - Cannot capture complex non-linear relationships

**Key Hyperparameters:**
- `C`: Controls regularization strength
- `penalty`: L1 / L2 regularization

---

### 2. Random Forest Classifier
- **Type:** Ensemble (Bagging)
- **Use case:** Strong general-purpose model
- **Strengths:**
  - Handles non-linear patterns
  - Reduces overfitting via averaging
  - Robust to noise
- **Limitations:**
  - Less interpretable
  - Slower than linear models

**Key Hyperparameters:**
- `n_estimators`: Number of trees
- `max_depth`: Tree depth
- `min_samples_split`
- `min_samples_leaf`

---

### 3. Neural Network (MLPClassifier)
- **Type:** Feed-forward neural network
- **Use case:** Capturing complex feature interactions
- **Strengths:**
  - Highly flexible
  - Learns non-linear representations
- **Limitations:**
  - Sensitive to scaling
  - Can overfit on small datasets
  - Less interpretable

**Key Hyperparameters:**
- `hidden_layer_sizes`
- `activation`
- `alpha` (L2 regularization)
- `max_iter`

---

### 4. XGBoost Classifier
- **Type:** Gradient Boosting
- **Use case:** High-performance model
- **Strengths:**
  - Excellent predictive power
  - Handles bias-variance tradeoff well
  - Works well on structured data
- **Limitations:**
  - More complex
  - Requires careful tuning

**Key Hyperparameters:**
- `n_estimators`
- `learning_rate`
- `max_depth`
- `subsample`
- `colsample_bytree`

---

## Evaluation Strategy

### Cross-Validation
- **Method:** Stratified K-Fold
- **Folds:** 5
- **Reason:**
  - Maintains class balance
  - Reduces overfitting
  - Provides reliable performance estimates

Each model was trained and evaluated across all folds, and **average metrics** were computed.

---

## Metrics Used

The following metrics were used for fair comparison:

| Metric        | Purpose |
|---------------|--------|
| Accuracy      | Overall correctness |
| Precision     | False positive control |
| Recall        | False negative control |
| F1-Score      | Balance between precision & recall |
| ROC-AUC       | Class separation capability |

---

## Model Selection Logic

1. Train all models using identical data splits
2. Evaluate using the same metrics
3. Compare **mean ROC-AUC and F1-Score**
4. Select the model with the **best overall generalization**
5. Save:
   - Best model (`best_model.pkl`)
   - Metrics summary (`metrics.json`)
   - Confusion matrix plot

---

## Final Outcome

- The best performing model was **automatically selected**
- Model artifacts were saved for inference and deployment
- This pipeline ensures:
  - Reproducibility
  - Fair comparison
  - Production readiness

---

## Key Learnings

- No single model is best for all datasets
- Cross-validation is essential for reliable evaluation
- Ensemble and boosting methods usually outperform simple models
- Metric selection should align with business goals
- Automated model comparison is an industry best practice
