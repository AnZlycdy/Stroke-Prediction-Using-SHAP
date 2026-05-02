# Explainable AI for Stroke Risk Prediction Using SHAP

An Explainable Artificial Intelligence (XAI) based healthcare application for predicting stroke risk using Machine Learning and SHAP explainability.

This MSc Research Project was developed as part of the **MSc Computer Science and Technology programme at Ulster University**. The project focuses on building a transparent and interpretable machine learning framework capable of predicting stroke risk while providing explainable insights into prediction outcomes.

---

## Project Overview

Stroke is one of the leading causes of death and long-term disability worldwide. Early prediction of stroke risk can support preventive healthcare interventions and improve patient outcomes.

This project implements:

- Machine Learning based stroke prediction
- Explainable AI (XAI) using SHAP
- Interactive Streamlit web application
- Real-time patient risk analysis
- Transparent prediction explanations

The system predicts stroke risk using patient demographic and clinical information such as:

- Age
- Hypertension
- Heart Disease
- BMI
- Glucose Level
- Smoking Status
- Marital Status
- Work Type

The project also integrates SHAP explainability to help users and healthcare professionals understand how different features contribute to prediction outcomes.

---

## Research Objectives

The objectives of this project were to:

- Develop an accurate stroke prediction system
- Compare multiple machine learning models
- Improve transparency using SHAP explainability
- Support trustworthy healthcare AI
- Analyse feature importance in stroke prediction

---


## Machine Learning Models Used

The project compares multiple machine learning approaches including:

- Logistic Regression
- Random Forest
- XGBoost

---

## Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Healthcare-focused metrics such as Recall and ROC-AUC were prioritised because false negatives in stroke prediction can be clinically dangerous.

---

## Explainable AI (XAI)

This project integrates **SHAP (SHapley Additive exPlanations)** to improve transparency and interpretability of healthcare predictions.

SHAP helps explain:

- which features influence predictions,
- how each feature contributes to risk,
- and why a patient is classified as high or low risk.

---

## Streamlit Application

The Streamlit application allows users to:

1. Enter patient clinical information
2. Predict stroke probability
3. View risk classification
4. Generate SHAP explainability visualisations

---

## Project Structure

```
Stroke-Prediction-Using-SHAP
├── app.py
├── Master_Project.ipynb
├── model.pkl
├── scaler.pkl
├── feature_names.pkl
├── label_encoders.pkl
├── X_train_scaled_df.pkl
├── requirements.txt
└── README.md
```

---

## Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Main programming language |
| Streamlit    | Web application framework |
| Scikit-learn | Machine learning          |
| XGBoost      | Gradient boosting model   |
| SHAP         | Explainable AI            |
| Pandas       | Data processing           |
| NumPy        | Numerical operations      |
| Matplotlib   | Visualisation             |
| Seaborn      | Data analysis             |

---

## Future Work

Future improvements for this project may include:

- Using larger real-world clinical datasets
- Exploring deep learning models for stroke prediction
- Comparing SHAP with other XAI techniques such as LIME

---

# Running the Application

Run the Streamlit application:

```bash
pip install -r requirements.txt
streamlit run app.py
```
---

## Author

**Anjali Chaudhary**  
MSc Computer Science and Technlogy  
Ulster University, United Kingdom  

Github: https://github.com/AnZlycdy/Stroke-Prediction-Using-SHAP

---

## Disclaimer

This project is developed for academic and educational purposes only and **NOT** be used for any professional medical diagnosis or clinical decision-making.
