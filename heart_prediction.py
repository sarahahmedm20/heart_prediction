# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 19:18:05 2023

@author: Sarah Ahmed
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/mgaaf/Desktop/final project Heart and diabetes prediction/ML/heart_disease_section_model.sav', 'rb'))


#prediction function

def heart_prediction(input_data):
    

    # converting data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # array reshaping as predicting for single instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'CONGRATULATIONS! you have no heart disease'
    else:
      return 'unfortunately you have heart disease,it is advised you book an appointment with a cardiologist in the app'
  
    
  
def main():
    

    st.title('welcome to MediHelp heart Prediction')
    
    age = st.slider('enter age',)
    gender = st.slider('your gender',0,1)
    chestpain = st.slider('level of chest pain',0,5)
    trestbps = st.slider('resting blood pressure',1,200)
    cholestrol = st.slider('your cholestrolr',0,300)
    fbs = st.slider('your fasting blood sugae level',0,2)
    thalach = st.slider('Max Heart rate',0,300)
    exerciseangina = st.slider('exercise angina value',0,10)
    oldpeak = st.slider('old peak',0,5)
    Thalassemia= st.slider('thalassemia value',0,4)


    diagnosis = ''
    
    # prediction button
    
    if st.button('heart prediction Test Result'):
           diagnosis = heart_prediction([ age, gender, chestpain, trestbps,cholestrol , fbs, thalach, exerciseangina,oldpeak, Thalassemia])
           
           
    st.success(diagnosis)
       
    
    
if __name__ == '__main__':
    main()