import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("customer_segmentation_pipeline.pkl", "rb"))

st.title("Customer Segmentation App")

# Inputs
age = st.number_input("Age")
work_exp = st.number_input("Work Experience")
family_size = st.number_input("Family Size")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Ever Married", ["Yes", "No"])
graduated = st.selectbox("Graduated", ["Yes", "No"])
profession = st.selectbox("Profession", ["Engineer", "Doctor", "Artist", "Lawyer", "Healthcare"])
spending = st.selectbox("Spending Score", ["Low", "Average", "High"])

if st.button("Predict Cluster"):
    data = pd.DataFrame({
        'Gender':[gender],
        'Ever_Married':[married],
        'Age':[age],
        'Graduated':[graduated],
        'Profession':[profession],
        'Work_Experience':[work_exp],
        'Spending_Score':[spending],
        'Family_Size':[family_size]
    })

    cluster = model.predict(data)[0]

    if cluster == 0:
        label = "Experienced Professionals"
    elif cluster == 1:
        label = "Senior Customers"
    else:
        label = "Young Families"

    st.success(f"Customer belongs to: {label}")