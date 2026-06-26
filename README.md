💳 End-to-end Credit Card Fraud Detection using Machine Learning with EDA, feature engineering, model evaluation, and fraud prediction.
This project demonstrates end-to-end ML workflow — from data analysis to model deployment.
# 💳 Fraud Detection System
## 🌐 Live Demo: https://fraud-detection-system-ruv4vgswqyo2mkpmqeah5c.streamlit.app/#fraud-detection-system.  
This project demonstrates end-to-end ML workflow — from data analysis to model deployment.

## 🚀 Project Overview

Financial fraud is rare but highly impactful. With only ~0.13% of transactions being fraudulent, this is a classic imbalanced classification problem that breaks naive models.

This project demonstrates a complete end-to-end ML workflow:

-  Raw data ingestion and cleaning
-  Exploratory Data Analysis on 6M+ transactions
-  Class imbalance handling using SMOTE
-  Training and comparing multiple ML models
-  Threshold tuning for real-world precision-recall tradeoff
-  Deployment via Streamlit web app
-  Cloud pipeline reproduction on Azure ML Designer

---

## 📂 Dataset

| Property | Details |
| Source | PaySim — Kaggle |
| Size | 6.3M+ transactions |
| Features | 7 (step, type, amount, balances) |
| Fraud Rate | ~0.13% (highly imbalanced) |
| Fraud Types | TRANSFER, CASH_OUT |

---

## Key Features

-  Deep EDA — transaction types, amount distributions, fraud patterns
-  SMOTE oversampling to handle extreme class imbalance
-  Benchmarked 3 models — Logistic Regression, Random Forest, XGBoost
-  Threshold tuning across 0.3 → 0.9 to optimize precision-recall
-  Live Streamlit app with real-time fraud prediction
-  3-tier risk scoring system (Legitimate / Suspicious / Fraudulent)
-  Prediction history tracking with visual distribution chart
-  Full pipeline reproduced on Azure ML Designer

---

## 🧪 Model Performance

**Final Model: Random Forest @ threshold 0.9**

| Metric | Score |
| Precision (Fraud) | 0.816 |
| Recall (Fraud) | 0.834 |
| F1-Score | 0.825 |
| ROC-AUC | 0.9985 |
| Accuracy | 99.95% |

### Threshold Tuning Results

| Threshold | Precision | Recall | F1 |
|---|---|---|---|
| 0.3 | 0.04 | 0.99 | 0.07 |
| 0.5 | 0.08 | 0.98 | 0.15 |
| 0.7 | 0.18 | 0.96 | 0.31 |
| **0.9** | **0.82** | **0.83** | **0.83** ✅ |

 💡 **Key Insight:** Accuracy is misleading here — predicting "no fraud" always gives 99.87%. Threshold selection is a business decision, not just a technical one.

## 🎯 3-Tier Risk Scoring (Streamlit App)

| Probability | Risk Level | Action |
| < 0.50 | ✅ Legitimate | Allow |
| 0.50 – 0.75 | ⚠️ Suspicious | Flag for review |
| > 0.75 | 🚨 Fraudulent | Block |

---

## ☁️ Azure ML Pipeline

Reproduced the complete pipeline on **Microsoft Azure ML Designer** to validate enterprise scalability.

**Pipeline Steps:**
```
Data Input → Clean Missing Data → Split Data → SMOTE → Train Model → Score Model → Evaluate Model
```

| Metric | Azure ML Result |
| AUC | 0.916 |
| Accuracy | 0.998 |

---

## ⚙️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost |
| Imbalance Handling | Imbalanced-learn (SMOTE) |
| Visualization | Matplotlib, Seaborn |
| Deployment | Streamlit |
| Cloud ML | Azure ML Designer |


## 📁 Project Structure
fraud-detection-system/
│
├── app.py                  # Streamlit web application
├── fraud_model.pkl         # Trained Random Forest model
├── paysimfraud.ipynb       # Complete ML notebook
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 💡 Key Learnings

- In imbalanced datasets, **accuracy is not a reliable metric**
- **SMOTE** effectively balances training data without losing information
- **Threshold tuning** is as important as model selection in production
- A **3-tier risk system** is more practical than a single binary threshold
- The same ML pipeline can be reproduced at **enterprise cloud scale** using Azure ML

---

## 👨‍💻 Developed By

**Ramandeep Singh**
