# -*- coding: utf-8 -*-
"""
Created on Tue Dec 16 12:21:25 2025

@author: U
"""

import streamlit as st
import pickle

# Load trained model
with open('SVM_model_GROUP_6.pkl', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("25rp19408")

# User input
st.write("Enter patient measurementsif malignant the patient has cancer if you get begnin he or she has no cancer:")

radius_mean = st.number_input("Radius Mean")
texture_mean = st.number_input("Texture Mean")
perimeter_mean = st.number_input("Perimeter Mean")
area_mean = st.number_input("Area Mean")

# Prediction button
if st.button("Predict"):
    input_data = [[radius_mean, texture_mean, perimeter_mean, area_mean]]
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("Prediction: Malignant")
    else:
        st.success("Prediction: Benign")

#cd C:\Users\U\Desktop\breastcancer
#dir to list

