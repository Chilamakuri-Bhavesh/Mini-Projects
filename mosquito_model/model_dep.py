#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score

import streamlit as st


st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Reckitt_%282021%29.svg/1200px-Reckitt_%282021%29.svg.png",
            width=200, # Manually Adjust the width of the image as per requirement
        )

asia_url ="https://github.com/Chilamakuri-Bhavesh/Mini-Projects/blob/main/mosquito_model/ASIA.csv?raw=true"
asia= pd.read_csv(asia_url)
asia.dropna(inplace=True)

europe_url = "https://github.com/Chilamakuri-Bhavesh/Mini-Projects/blob/main/mosquito_model/EUROPE.csv?raw=true"
europe=pd.read_csv(europe_url)


asia.drop(["Unnamed: 0"],axis = 1 , inplace =True)
#europe.drop(["Unnamed: 0"],axis = 1 , inplace =True)

label_encoder = LabelEncoder()
asia["Country"]=label_encoder.fit_transform(asia['Country'])
europe["Country"]=label_encoder.fit_transform(europe['Country'])


x_train= asia.iloc[:,:-1]
y_train= asia.iloc[:,-1:]
#x_test= europe.iloc[:,:-1]
y_test= europe.iloc[:,-1:]

dt_regressor = DecisionTreeRegressor()
dt_regressor.fit(x_train, y_train)


st.title("DENGUE CASES PER 100,000 PEOPLE PREDICTION ALGORITHM")

st.subheader("ENTER THE VALUES : ")


c_name = [ "Austri",
    "Belgium",
    "Croatia",
    "Czechia",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Iceland",
    "Ireland",
    "Italy",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "United Kingdom"
]

Country_Name = st.selectbox(
    'Select a Country',
     ("Austri",
    "Belgium",
    "Croatia",
    "Czechia",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Iceland",
    "Ireland",
    "Italy",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Norway",
    "Poland",
    "Portugal",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "United Kingdom"
))


for i in c_name:
    if Country_Name == "Austri":
        c_n = 0
    elif Country_Name == "Belgium":
         c_n = 1
    elif Country_Name == "Croatia":
         c_n = 2
    elif Country_Name == "Czechia":
         c_n = 3
    elif Country_Name == "Estonia":
         c_n = 4
    elif Country_Name == "Finland":
         c_n = 5
    elif Country_Name == "France":
         c_n = 6
    elif Country_Name == "Germany":
         c_n = 7
    elif Country_Name == "Greece":
         c_n = 8
            
    elif Country_Name == "Hungary":
         c_n = 9
            
    elif Country_Name == "Iceland":
         c_n = 10
    elif Country_Name == "Ireland":
         c_n = 11
            
    elif Country_Name == "Italy":
         c_n = 12
            
    elif Country_Name == "Latvia":
         c_n = 13
            
    elif Country_Name == "Lithuania":
         c_n = 14
    elif Country_Name == "Luxembourg":
         c_n = 15
    elif Country_Name == "Malta":
         c_n = 16
    elif Country_Name == "Netherlands":
         c_n = 17
    elif Country_Name == "Norway":
         c_n = 18
    elif Country_Name == "Poland":
         c_n = 19
    elif Country_Name == "Portugal":
         c_n = 20
    elif Country_Name == "Romania":
         c_n = 21
    elif Country_Name == "Slovakia":
         c_n = 22
    elif Country_Name == "Slovenia":
         c_n = 23
    elif Country_Name == "Spain":
         c_n = 24
    elif Country_Name == "Sweden":
         c_n = 25
    elif Country_Name == "United Kingdom":
         c_n = 26
       
    

Year =  st.number_input("Enter the Year")

Temperature = st.number_input("Enter the Average Temperature (Celsius (°C))")

Wind_Speed = st.number_input("Enter the Average Wind Speed (m/s) ")

Average_Relative_Humidity  = st.number_input("Enter the Average Relative Humidity (%)")

Geographic_Average_Precipitation = st.number_input("Enter the Geographic_Average Precipitation (mm/day)")


di={"Country":c_n,"Year":Year,"Geographic_Average Temperature at 2 Meters (Celsius (°C))":Temperature,
        "Geographic_Average Wind Speed at 10M Range (m/s)":Wind_Speed,
            "Geographic_Average Relative Humidity at 2 Meters (%) ":Average_Relative_Humidity,
    "Geographic_Average Precipitation (mm/day)":Geographic_Average_Precipitation}

x_test=pd.DataFrame([di])
y_pred = dt_regressor.predict(x_test)

result = y_pred

st.subheader("PREDICTED DENGUE CASES PER 100,000 PEOPLE : ")
st.write(result)

