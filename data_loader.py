import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv("credit_customers (DS).csv")
    return data

def preprocess_data(data):
    # One-hot encode categorical columns
    categorical_columns = ["checking_status", "credit_history", "purpose", "savings_status", "employment", 
                           "personal_status", "other_parties", "property_magnitude", "other_payment_plans", 
                           "housing", "job", "own_telephone", "foreign_worker"]
    data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)
    return data