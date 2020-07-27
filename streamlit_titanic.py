import streamlit as st
import joblib
import pandas as pd
import numpy as np

from PIL import Image

model = open("rf_titanic.pkl", "rb")
classifier = joblib.load(model)

st.title("TITANIC DATASET -- ENTER VALUES TO CHECK WHETHER THE PASSENGER WOULD HAVE SURVIVED")

st.sidebar.title("Choose the description of the person:")
name=st.sidebar.text_input(label="Enter the name of the passenger")
parameter_list = ["Sex", "Age", "Pclass", "Fare"]

parameter_input = []
parameter_default_values= ["Male","25.0","1.0","70.0"]
#col = parameter_list_num + parameter_list_class

values=[]

for p, p_df in zip(parameter_list, parameter_default_values):
    if p=="Age" :
        
        values= st.sidebar.slider(label="Select age of the person", key=p, value=float(p_df), min_value=0.0, max_value=100.0, step=0.1)
        
    elif p=="Fare":
        values= st.sidebar.slider(label="Select fare of his ticket", key=p, value=float(p_df), min_value=0.0, max_value=250.0, step=0.1)
        
    elif p=="Sex":
        values = st.sidebar.radio(label='Choose Sex of passenger', options=[ 'Female', 'Male'])
        
    else:
        values = st.sidebar.radio(label='Choose Class the passenger travelled in', options=[1.0, 2.0, 3.0])
        
        
    
        
    
    parameter_input.append(values)
    


if(parameter_input[0]=="Male"):
    parameter_input[0] = 0.0
    parameter_input.insert(1,1.0)
else:
    parameter_input[0]= 1.0
    parameter_input.insert(1,0.0)
    

  

st.write("\n\n")

dead= Image.open("dead.png")
alive = Image.open("alive.png")


if st.button("Click to predict whether the passenger would have survived"):
    prediction = classifier.predict([parameter_input])
    if prediction==0:
        st.write("Sorry, "+name+" You would have Died :(")
        st.image(dead)
    else:
        st.write("Congratulations "+name+" ! You would have Survived!!:D")
        st.image(alive)
    