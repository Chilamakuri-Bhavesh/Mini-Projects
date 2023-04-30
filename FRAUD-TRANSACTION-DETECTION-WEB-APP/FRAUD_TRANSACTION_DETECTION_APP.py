#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import pandas as pd

import sklearn
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import classification_report , accuracy_score, r2_score

from sklearn.tree import DecisionTreeClassifier

import streamlit as st

url="https://raw.githubusercontent.com/Chilamakuri-Bhavesh/Mini-Projects/main/FRAUD-TRANSACTION-DETECTION-WEB-APP/data_set.csv"

df=pd.read_csv(url, sep="\t") 

#df["type"] = df["type"].map({"CASH_OUT":1,"PAYMENT":2,"CASH_IN":3,"TRANSFER":4,"DEBIT":5})  #already converted

x=np.array(df[["type","amount","oldbalanceOrg","newbalanceOrig"]])

y=np.array(df[["isFraud"]])

x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,train_size=0.8)

dtc = DecisionTreeClassifier()

dtc.fit(x_train,y_train)

st.title("ENTER THE DETAILS TO FIND WHETHER A TRANSACTION IS FRAUD OR NOT FRAUD")

st.text("DIFFERENT TYPES OF PAYMENTS ARE :")

st.text("CASH_OUT = 1, PAYMENT = 2, CASH_IN = 3, TRANSFER = 4, DEBIT = 5")

payment_type = st.number_input("Enter the Payment Type Number ")

amount= st.number_input("Enter the Amount")

old_balance = st.number_input("Enter the Old Balance")

new_balance = st.number_input("Enter the New Balance")

output=np.array([[payment_type,amount,old_balance,new_balance]])


predictions = dtc.predict(output)

st.header("THE TRANSCATION IS")

def out_put():
    if predictions == 0:
        r="Not Fraud"
    else:
        r="Fraud"
        
    return r

result = out_put()

st.write(result)

