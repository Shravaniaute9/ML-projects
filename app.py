# -*- coding: utf-8 -*-

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("salary_model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(YearsExperience):
   
    prediction=classifier.predict([[YearsExperience]])
    print(prediction)
    return prediction



def main():
    st.title("\t Salary Prediction of Employee")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h3 style="color:white;text-align:center;">Streamlit salary prdiction ML App </h3>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    YearsExperience = st.text_input("YearsExperience","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(eval(YearsExperience))
    st.success('The output is {} $'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("This is about saraly prediction of employee based on year of experiance.")
        st.text("The employees experiance should be more than zero years.")      

if __name__=='__main__':
    main()
    
    
    