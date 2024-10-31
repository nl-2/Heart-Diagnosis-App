import streamlit as st
import numpy as np
import pickle

# Load the saved heart disease prediction model
model = pickle.load(open('heartt_model.sav', 'rb'))

# Streamlit app
st.title('Heart Disease Prediction System')

# Collect user input for model features
age = st.number_input('Age', min_value=1, max_value=120)
sex = st.selectbox('Sex', ['Female', 'Male'])
cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200)
chol = st.number_input('Cholesterol Level', min_value=100, max_value=400)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'])
restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'Having ST-T Wave Abnormality', 'Showing Probable or Definite Left Ventricular Hypertrophy'])
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220)
exang = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
oldpeak = st.number_input('ST Depression Induced by Exercise')
slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Upsloping', 'Flat', 'Downsloping'])
ca = st.selectbox('Number of Major Vessels', [0, 1, 2, 3, 4])
thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

# Map text inputs to numerical values for the model
sex = 1 if sex == 'Male' else 0
cp = ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'].index(cp)
fbs = 1 if fbs == 'Yes' else 0
restecg = ['Normal', 'Having ST-T Wave Abnormality', 'Showing Probable or Definite Left Ventricular Hypertrophy'].index(restecg)
exang = 1 if exang == 'Yes' else 0
slope = ['Upsloping', 'Flat', 'Downsloping'].index(slope)
thal = ['Normal', 'Fixed Defect', 'Reversible Defect'].index(thal)

# Prepare input data for prediction
input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
input_data = np.asarray(input_data).reshape(1, -1)

# Predict and display result
if st.button('Predict'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("The model predicts the presence of heart disease.")
    else:
        st.success("The model predicts no presence of heart disease.")
