# 🧠 Explainable AI for Stroke Risk Prediction Using SHAP

An Explainable Artificial Intelligence (XAI) based healthcare application for predicting stroke risk using Machine Learning and SHAP explainability.

This MSc Research Project was developed as part of the **MSc Computer Science and Technology programme at Ulster University**. The project focuses on building a transparent and interpretable machine learning framework capable of predicting stroke risk while providing explainable insights into prediction outcomes.

---

# 📌 Project Overview

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

# 🚀 Features

✅ Stroke Risk Prediction using Machine Learning  
✅ Interactive Streamlit User Interface  
✅ SHAP Waterfall Plot Explanations  
✅ SHAP Feature Importance Visualisation  
✅ Patient Risk Categorisation (Low / Moderate / High)  
✅ Real-Time Prediction Probability  
✅ Explainable Healthcare AI Framework

---

# 🧠 Machine Learning Models Used

The project compares multiple machine learning approaches including:

- Logistic Regression
- Random Forest
- XGBoost

The final deployed model was selected based on:

- Recall
- ROC-AUC
- Explainability
- Clinical interpretability

---

# 📊 Explainable AI (XAI)

This project integrates **SHAP (SHapley Additive exPlanations)** to improve transparency and interpretability of healthcare predictions.

SHAP helps explain:

- which features influence predictions,
- how each feature contributes to risk,
- and why a patient is classified as high or low risk.

The application generates:

- SHAP Waterfall Plots
- SHAP Bar Plots
- Feature Contribution Analysis

---

# 🖥️ Streamlit Application

The Streamlit application allows users to:

1. Enter patient clinical information
2. Predict stroke probability
3. View risk classification
4. Generate SHAP explainability visualisations

---

# 📂 Project Structure

```text
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

# ⚙️ Technologies Used

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

# ▶️ Running the Application

Run the Streamlit application:

```bash
pip install -r requirements.txt
streamlit run app.py
```

The application will open in your browser.

---

# 📈 Dataset

Dataset used:

- Stroke Prediction Dataset (Kaggle)

Features include:

- Gender
- Age
- Hypertension
- Heart Disease
- Average Glucose Level
- BMI
- Smoking Status
- Residence Type
- Work Type

---

# 📌 Research Objectives

The objectives of this project were to:

- Develop an accurate stroke prediction system
- Compare multiple machine learning models
- Improve transparency using SHAP explainability
- Support trustworthy healthcare AI
- Analyse feature importance in stroke prediction

---

# 📊 Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

Healthcare-focused metrics such as Recall and ROC-AUC were prioritised because false negatives in stroke prediction can be clinically dangerous.

---

# 🔍 Example SHAP Outputs

The system provides:

- SHAP Waterfall Plot
- SHAP Bar Plot
- Feature Importance Analysis

These explainability techniques improve clinician trust and transparency in AI-assisted healthcare systems.

---

# ⚠️ Disclaimer

This project was developed for:

- educational,
- academic,
- and research purposes only.

It should **NOT** be used as a substitute for professional medical diagnosis or clinical decision-making.

---

# 📚 Research Contribution

This project contributes toward:

- Explainable Artificial Intelligence in healthcare
- Transparent machine learning systems
- Stroke prediction research
- Trustworthy AI frameworks

---

# 👩‍💻 Author

**Anjali Chaudhary**  
MSc Computer Science  
Ulster University

---

# 📜 License

This project is intended for academic and educational purposes.
