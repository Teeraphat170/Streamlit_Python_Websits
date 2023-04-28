from firebase import firebase
import pandas as pd
import time
import numpy as np
import streamlit as st
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import numpy as np
import pandas as pd
# from Predict import predict
import statistics
import pickle
import time
from datetime import datetime
from scipy.stats import kurtosis
from firebase import firebase
from firebase_admin import db
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")


firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
result = firebaseDB.get('/FinalProject', '')
# firebaseDB.delete('/FinalProject','')
st.set_page_config(layout="wide")
df = pd.DataFrame()
for key, value in result.items():
    Prediction = value["Prediction"]
    Probability = value["Probability"]
    Result = value["Result"]
    Time = value["Time"]
    Std3 = value["Std3"]
    Std2 = value["Std2"]
    Mean2 = value["Mean2"]
    Std1 = value["Std1"]
    PToP1 = value["PToP1"]
    PToP4 = value["PToP4"]
    PToP2 = value["PToP2"]
    Std4 = value["Std4"]
    Kurtosis1 = value["Kurtosis1"]
    Kurtosis4 = value["Kurtosis4"]

    Data = {"Prediction":[Prediction],"Probability":[Probability],"Result":[Result],"Time":[Time],"Std3":[Std3],
                    "Std2":[Std2],"Mean2":[Mean2],"Std1":[Std1],"PToP1":[PToP1],"PToP4":[PToP4],
                    "PToP2":[PToP2],"Std4":[Std4],"Kurtosis1":[Kurtosis1],"Kurtosis4":[Kurtosis4],}
            
    Data = pd.DataFrame(Data)
    df = pd.concat([df, Data], axis=0)

df = df.reset_index(drop=True)
DataQ = df[["Prediction","Probability","Std3","Std2","Mean2","Std1","PToP1","PToP4","PToP2","Std4","Kurtosis1","Kurtosis4","Time"]]

Prediction = pd.DataFrame()
Prediction = df["Prediction"]
# DataQ = DataQ.set_index('Time')
# Test = df[["Prediction","Probability","Std3"]]
fig = px.line(DataQ, x='Time',y=DataQ.columns[:-1])
# TimeX = df["Time"]
# print(DataQ)
# # print(df)
# st.line_chart(DataQ ,x=DataQ.index)
col2, col3 = st.columns((30,30))
with col2:
    st.line_chart(Prediction)
with col3:
    st.dataframe(df)

col3.markdown(
    """
    <style>
    .st-b8 {
        border: 2px solid black;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

col2.markdown(
    """
    <style>
    .st-b9 {
        border: 2px solid black;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
        
