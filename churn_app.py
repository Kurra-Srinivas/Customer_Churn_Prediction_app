#Gender-->1 female and 0 male
#churn-->1 yes and 0 no
#scaler is exported as scaler.pkl
# model is exported as model.pkl
#order of x-->'Age', 'Gender', 'Tenure', 'MonthlyCharges'

import streamlit as st
import numpy as np
import joblib

scaler=joblib.load("scaler.pkl")
model=joblib.load("model.pkl")

st.title("Customer Churn Prediction app")

st.divider()

st.write("Please enter the values and hit the predict button.")

st.divider()

age=st.number_input("Enter Age", min_value=10, max_value=100, value=30, step=1)

tenure=st.number_input("Enter Tenure", min_value=0, max_value=130, value=10, step=1)

monthlycharges=st.number_input("Enter Monthly Charges", min_value=30, max_value=150)

gender=st.selectbox("Enter the Gender",["Male","Female"])

st.divider()


predictions=st.button("Predict")

if predictions:

    gender_selected=1 if gender =="Female" else 0

    x=[age,gender_selected,tenure,monthlycharges]

    x1=np.array(x)

    x_array=scaler.transform([x1])

    prediction=model.predict(x_array)[0]

    prediction="Yes" if prediction==1 else "No"

    st.write(f"Churn Predicted: {prediction}")

else:
    st.write("Please enter the values and hit the predict button.")










