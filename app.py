import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("insuarance_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Insurance Charges Prediction",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Insurance Charges Prediction")
st.write("Enter the details below to predict insurance charges.")

# User inputs
age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=25
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

is_female = 1 if gender == "Female" else 0

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.selectbox(
    "Smoker",
    ["No", "Yes"]
)

is_smoker = 1 if smoker == "Yes" else 0

region = st.selectbox(
    "Region",
    ["Northeast", "Northwest", "Southeast", "Southwest"]
)

region_southeast = 1 if region == "Southeast" else 0

bmi_category = st.selectbox(
    "BMI Category",
    ["Normal/Overweight", "Obese"]
)

bmi_category_Obese = 1 if bmi_category == "Obese" else 0


# Prediction
if st.button("Predict Insurance Charges"):

    input_data = pd.DataFrame([{
        "age": age,
        "is_female": is_female,
        "bmi": bmi,
        "children": children,
        "is_smoker": is_smoker,
        "region_southeast": region_southeast,
        "bmi_category_Obese": bmi_category_Obese
    }])

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated Insurance Charges: ₹{prediction:,.2f}"
    )