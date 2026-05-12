import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Fraud Detection System", page_icon="💳", layout="wide")

# model
model = joblib.load("fraud_model.pkl")

# sidebar
st.sidebar.title("About")
st.sidebar.info("Machine Learning based Fraud Detection System ")


# main title

st.title("💳 Fraud Detection System")

# user input
step = st.number_input("Step", min_value=1, value=1)

type_transaction = st.selectbox(
    "Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT"]
)

amount = st.number_input("Amount", min_value=0.0)

oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0)

newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0)

oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0)

newbalanceDest = st.number_input("New Balance Destination", min_value=0.0)


# Encoding transaction type
type_mapping = {"PAYMENT": 0, "TRANSFER": 1, "CASH_OUT": 2, "DEBIT": 3}

type_encoded = type_mapping[type_transaction]

if st.button("Predict Fraud"):
    if amount > oldbalanceOrg:
        st.error("Invalid transaction: insufficient balance")

    else:
        new_input = {
            "step": step,
            "type": type_encoded,
            "amount": amount,
            "oldbalanceOrg": oldbalanceOrg,
            "newbalanceOrig": newbalanceOrig,
            "oldbalanceDest": oldbalanceDest,
            "newbalanceDest": newbalanceDest,
        }

        new_df = pd.DataFrame([new_input])

        fraud_probability = model.predict_proba(new_df)[0][1]

    # result on basis of probality

    if fraud_probability < 0.5:
        result = "Legitimate"
        st.success("✅ Legitimate Transaction")

    elif fraud_probability < 0.75:
        result = "Suspicious"
        st.warning("⚠️ Suspicious Transaction")

    else:
        result = "Fraudulent"
        st.error("🚨 Fraudulent Transaction")

    # Showcasing probability here
    st.write(f"Fraud Probability: {fraud_probability:.2f}")

    # Progress bar
    st.progress(float(fraud_probability))

    history = pd.DataFrame(
        [
            {
                "Step": step,
                "Type": type_transaction,
                "Amount": amount,
                "OldBalanceOrg": oldbalanceOrg,
                "NewBalanceOrig": newbalanceOrig,
                "OldBalanceDest": oldbalanceDest,
                "NewBalanceDest": newbalanceDest,
                "FraudProbability": round(fraud_probability, 2),
                "Result": result,
            }
        ]
    )

    file_exists = os.path.isfile("transaction_history.csv")

    history.to_csv(
        "transaction_history.csv", mode="a", header=not file_exists, index=False
    )
# transaction history
st.subheader("📜 Transaction History")

try:
    history_df = pd.read_csv("transaction_history.csv")

    st.dataframe(history_df.tail(10))

    # metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Model", "Random Forest")
    col2.metric("Threshold", "0.75")
    col3.metric("ROC-AUC", "0.99")

    # creating pie chart:
    counts = history_df["Result"].value_counts()

    fig, ax = plt.subplots()

    ax.pie(counts, labels=counts.index, autopct="%1.1f%%")

    st.subheader("📊 Transaction Distribution")
    st.pyplot(fig)

except FileNotFoundError:
    st.info("No transaction history found. Start by making a prediction!")

# Footer
st.caption("Developed by Ramandeep Singh")
