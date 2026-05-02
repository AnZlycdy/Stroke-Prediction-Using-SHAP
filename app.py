import streamlit as st
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Stroke Risk Prediction",
    page_icon="🧠",
    layout="wide"
)

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label_encoders = pickle.load(open("label_encoders.pkl", "rb"))
feature_names = pickle.load(open("feature_names.pkl", "rb"))
shap_background = pickle.load(open("X_train_scaled_df.pkl", "rb"))

st.markdown(
    """
    <h1 style='text-align: center;'>🧠 Stroke Risk Prediction</h1>
    <p style='text-align: center; font-size:18px; color:gray;'>
        Machine Learning Based Stroke Risk Assessment
    </p>
    """,
    unsafe_allow_html=True
)
st.warning(
    "This prototype is developed for educational and research purposes only "
    "and should not be used as a substitute for professional medical advice or diagnosis."
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=0, max_value=120, value=45)
    hypertension = st.selectbox("Hypertension", [0, 1])

with col2:
    heart_disease = st.selectbox("Heart Disease", [0, 1])
    ever_married = st.selectbox("Ever Married", ["Yes", "No"])
    work_type = st.selectbox(
        "Work Type",
        ["Private", "Self-employed", "Govt_job", "children", "Never_worked"]
    )

with col3:
    residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
    avg_glucose_level = st.number_input(
        "Average Glucose Level",
        min_value=0.0,
        max_value=300.0,
        value=100.0
    )
    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=80.0,
        value=25.0
    )
    smoking_status = st.selectbox(
        "Smoking Status",
        ["formerly smoked", "never smoked", "smokes", "Unknown"]
    )

input_data = pd.DataFrame({
    "gender": [gender],
    "age": [age],
    "hypertension": [hypertension],
    "heart_disease": [heart_disease],
    "ever_married": [ever_married],
    "work_type": [work_type],
    "Residence_type": [residence_type],
    "avg_glucose_level": [avg_glucose_level],
    "bmi": [bmi],
    "smoking_status": [smoking_status]
})

original_input = input_data.copy()

for col, le in label_encoders.items():
    input_data[col] = le.transform(input_data[col].astype(str))

input_data = input_data[feature_names]

input_scaled = scaler.transform(input_data)
input_scaled_df = pd.DataFrame(input_scaled, columns=feature_names)

st.markdown("---")

if st.button("Predict Stroke Risk", width="stretch"):

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.subheader("Prediction Result")

    r1, r2, r3 = st.columns(3)

    with r1:
        st.metric("Stroke Probability", f"{probability:.2%}")

    with r2:
        if prediction == 1:
            st.error("High Risk")
        else:
            st.success("Low Risk")

    with r3:
        if probability < 0.30:
            st.metric("Risk Level", "Low")
        elif probability < 0.60:
            st.metric("Risk Level", "Moderate")
        else:
            st.metric("Risk Level", "High")

    st.markdown("---")

    st.subheader("Patient Data")
    st.dataframe(original_input, width="stretch")

    st.markdown("---")

    st.subheader("SHAP Explanation")

    explainer = shap.Explainer(model, shap_background)
    shap_values = explainer(input_scaled_df)

    st.write("SHAP Waterfall Plot")
    fig = plt.figure(figsize=(10, 6))
    shap.plots.waterfall(shap_values[0], show=False)
    st.pyplot(fig)

    st.write("SHAP Bar Plot")
    fig2 = plt.figure(figsize=(10, 6))
    shap.plots.bar(shap_values[0], show=False)
    st.pyplot(fig2)