# 💳 Fraud Detection System
## 🌐 Live Demo: https://fraud-detection-system-ruv4vgswqyo2mkpmqeah5c.streamlit.app/#fraud-detection-system

A machine learning-based fraud detection system that identifies suspicious financial transactions in real-time.  
This project demonstrates end-to-end ML workflow — from data analysis to model deployment.

## 🚀 Project Overview

Financial fraud is rare but highly impactful.  
In this project, I built a system that can:

- Detect fraudulent transactions
- Handle highly imbalanced data
- Provide real-time predictions via a web app

The system is deployed using **Streamlit** and uses a trained **Random Forest model**.

---

## Key Features

- 📊 Exploratory Data Analysis (EDA) on 6M+ transactions  
- ⚖️ Handled class imbalance using SMOTE  
- 🤖 Built and compared multiple models:
  - Logistic Regression  
  - Random Forest  
  - XGBoost  
- 🎯 Threshold tuning for precision-recall optimization  
- 🌐 Deployed using Streamlit for real-time predictions  
- 📈 Tracks prediction history and visualizes results  

---

## 🧪 Model Performance

Final model: **Random Forest**

-  Precision (Fraud): ~0.81  
-  Recall (Fraud): ~0.83  
-  F1 Score: ~0.82  
-  ROC-AUC: ~0.99  

A custom threshold of **0.9** was selected to balance false positives and fraud detection effectively.

---

## ⚙️ Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Imbalanced-learn (SMOTE)  
- Matplotlib, Seaborn  
- Streamlit  

---


cd fraud-detection-system
pip install -r requirements.txt
streamlit run app.py
