# 💳 Credit Card Fraud Detection System

An end-to-end **Machine Learning** project for detecting fraudulent financial transactions using **Exploratory Data Analysis (EDA), feature engineering, class imbalance handling (SMOTE), model evaluation, threshold tuning, and an interactive Streamlit dashboard**.

## 🌐 Live Demo

**Try the deployed application here:**

👉 https://fraud-detection-system-ruv4vgswqyo2mkpmqeah5c.streamlit.app/

---

# 📌 Project Overview

Credit card fraud is one of the biggest challenges faced by financial institutions. Since fraudulent transactions represent only a tiny fraction of all transactions, detecting them accurately while minimizing false alarms is a challenging machine learning problem.

This project builds a complete fraud detection pipeline—from data preprocessing and exploratory analysis to model training, evaluation, deployment, and cloud implementation.

The final solution enables users to enter transaction details and instantly receive a fraud prediction with an associated risk level.

---

# 🎯 Objectives

* Analyze transaction patterns through Exploratory Data Analysis (EDA)
* Handle extreme class imbalance using SMOTE
* Train and compare multiple machine learning models
* Optimize prediction threshold for real-world performance
* Deploy the final model using Streamlit
* Reproduce the workflow using Microsoft Azure ML Designer

---

# 📂 Dataset

**Dataset:** PaySim Mobile Money Transactions (Kaggle)

### Dataset Summary

* 📄 Over **6.3 million** transaction records
* 📈 Highly imbalanced dataset (~0.13% fraudulent transactions)
* 💳 Mobile money transaction simulation
* 🚨 Fraud primarily occurs in **TRANSFER** and **CASH_OUT** transaction types

### Dataset Features

| Feature        | Description                                   |
| -------------- | --------------------------------------------- |
| step           | Time step representing the hour of simulation |
| type           | Transaction type                              |
| amount         | Transaction amount                            |
| oldbalanceOrg  | Sender balance before transaction             |
| newbalanceOrig | Sender balance after transaction              |
| oldbalanceDest | Receiver balance before transaction           |
| newbalanceDest | Receiver balance after transaction            |
| isFraud        | Fraud label (Target Variable)                 |

---

# 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Imbalanced-learn (SMOTE)
* Streamlit
* Microsoft Azure ML Designer
* Jupyter Notebook

---

# 🔬 Machine Learning Workflow

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Handling Class Imbalance using SMOTE
* Model Training
* Model Evaluation
* Threshold Optimization
* Streamlit Deployment
* Azure ML Pipeline Implementation

---

# 🤖 Models Evaluated

* Logistic Regression
* Random Forest
* XGBoost

The Random Forest classifier delivered the best balance between precision and recall after threshold tuning.

---

# 📊 Model Performance

### Final Model: Random Forest (Threshold = 0.90)

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 99.95% |
| Precision | 0.816  |
| Recall    | 0.834  |
| F1 Score  | 0.825  |
| ROC-AUC   | 0.9985 |

---

# ⚖️ Threshold Tuning Results

| Threshold | Precision |   Recall |   F1 Score |
| --------- | --------: | -------: | ---------: |
| 0.30      |      0.04 |     0.99 |       0.07 |
| 0.50      |      0.08 |     0.98 |       0.15 |
| 0.70      |      0.18 |     0.96 |       0.31 |
| **0.90**  |  **0.82** | **0.83** | **0.83** ✅ |

### Key Insight

Instead of relying solely on accuracy, threshold tuning significantly improved fraud detection performance by balancing precision and recall, making the model more practical for real-world financial applications.

---

# 🚨 Fraud Risk Classification

The deployed application categorizes predictions into three risk levels:

| Fraud Probability | Risk Level    | Recommended Action  |
| ----------------: | ------------- | ------------------- |
|            < 0.50 | ✅ Legitimate  | Approve Transaction |
|       0.50 – 0.75 | ⚠️ Suspicious | Manual Review       |
|            > 0.75 | 🚨 Fraudulent | Block Transaction   |

---

# ☁️ Azure ML Implementation

The machine learning pipeline was also recreated using **Microsoft Azure ML Designer** to demonstrate how the workflow can be implemented in a cloud-based enterprise environment.

Pipeline:

```text
Data Input
      ↓
Data Cleaning
      ↓
Train/Test Split
      ↓
SMOTE
      ↓
Train Model
      ↓
Score Model
      ↓
Evaluate Model
```

Azure Evaluation Metrics

| Metric   | Score |
| -------- | ----: |
| Accuracy | 99.8% |
| AUC      | 0.916 |

---

# 📈 Exploratory Data Analysis

The project includes comprehensive visual analysis, including:

* Fraud vs Legitimate Transactions
* Transaction Type Distribution
* Transaction Amount Distribution
* Correlation Heatmap
* Fraud Distribution by Transaction Type
* Balance Change Analysis
* Feature Relationships

---

# 📸 Project Preview
<img width="1907" height="998" alt="Screenshot 2026-06-27 004100" src="https://github.com/user-attachments/assets/18c46fda-8cdc-4db0-a087-f0c2b93a1137" />
<img width="862" height="679" alt="Screenshot 2026-06-27 004158" src="https://github.com/user-attachments/assets/13e50488-8ef5-401d-a9c8-a6081b03e0ef" />
<img width="804" height="532" alt="Screenshot 2026-06-27 004223" src="https://github.com/user-attachments/assets/3a5e78fb-44a6-4c65-befb-af83f9372906" />
<img width="539" height="693" alt="Screenshot 2026-06-27 004247" src="https://github.com/user-attachments/assets/061320d1-770f-427a-8c14-53ab5567cc91" />


---

# 📁 Project Structure

```text
fraud-detection-system/
│
├── app.py
├── paysimfraud.ipynb
├── fraud_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── images/
```

---

# ▶️ Getting Started

### Clone the Repository

```bash
git clone https://github.com/ramandeepp1403/fraud-detection-system.git
```

### Navigate to the Project

```bash
cd fraud-detection-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit App

```bash
streamlit run app.py
```

---

# 💡 Key Learnings

* Handling highly imbalanced datasets using SMOTE
* Importance of precision and recall in fraud detection
* Threshold tuning for production-ready machine learning models
* Building interactive ML applications with Streamlit
* Deploying machine learning workflows on Azure ML Designer
* End-to-end model development and deployment

---

# 🚀 Future Improvements

* Real-time API integration
* Explainable AI using SHAP
* Model monitoring dashboard
* Cloud deployment using Docker and Azure
* Automated model retraining pipeline

---

# 👨‍💻 Developed By

**Ramandeep Singh**

* GitHub: https://github.com/ramandeepp1403
* LinkedIn: https://www.linkedin.com/in/ramandeep-pandi/

---

# ⭐ Support

If you found this project useful, consider giving the repository a **⭐ Star**.
