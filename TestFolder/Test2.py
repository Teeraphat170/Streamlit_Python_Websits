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


# firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
# result = firebaseDB.get('/FinalProject', '')
# # firebaseDB.delete('/FinalProject','')
# st.set_page_config(layout="wide")
# df = pd.DataFrame()
# for key, value in result.items():
#     Prediction = value["Prediction"]
#     Probability = value["Probability"]
#     Result = value["Result"]
#     Time = value["Time"]
#     Std3 = value["Std3"]
#     Std2 = value["Std2"]
#     Mean2 = value["Mean2"]
#     Std1 = value["Std1"]
#     PToP1 = value["PToP1"]
#     PToP4 = value["PToP4"]
#     PToP2 = value["PToP2"]
#     Std4 = value["Std4"]
#     Kurtosis1 = value["Kurtosis1"]
#     Kurtosis4 = value["Kurtosis4"]

#     Data = {"Prediction":[Prediction],"Probability":[Probability],"Result":[Result],"Time":[Time],"Std3":[Std3],
#                     "Std2":[Std2],"Mean2":[Mean2],"Std1":[Std1],"PToP1":[PToP1],"PToP4":[PToP4],
#                     "PToP2":[PToP2],"Std4":[Std4],"Kurtosis1":[Kurtosis1],"Kurtosis4":[Kurtosis4],}
            
#     Data = pd.DataFrame(Data)
#     df = pd.concat([df, Data], axis=0)

# df = df.reset_index(drop=True)
# DataQ = df[["Prediction","Probability","Std3","Std2","Mean2","Std1","PToP1","PToP4","PToP2","Std4","Kurtosis1","Kurtosis4","Time"]]

# Prediction = pd.DataFrame()
# Prediction = df["Prediction"]
# # DataQ = DataQ.set_index('Time')
# # Test = df[["Prediction","Probability","Std3"]]
# fig = px.line(DataQ, x='Time',y=DataQ.columns[:-1])
data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')
data1 = pd.read_csv('Component/Data/Dataset/All134.csv')
Ex = data.reset_index(drop=True)
Ex1 = data1.reset_index(drop=True)

new = Ex[["level_2","level_3","level_4","level_5","[LOGGING]","RD81DL96_1","2","3","4"]]


data = {
  "calories": [420, 380, 390, 380, 400, 390],
  "duration": [50, 40, 45, 50, 50, 45],
  "test":[12, 16, 15, 16, 15, 19],
    "calories1": [420, 380, 390, 380, 400, 390],
  "duration1": [50, 40, 45, 50, 50, 45],
  "test1":[12, 16, 15, 16, 15, 19],
    "calories3": [420, 380, 390, 380, 400, 390],
  "duration3": [50, 40, 45, 50, 50, 45],
  "test3":[12, 16, 15, 16, 15, 19],
    "calories4": [420, 380, 390, 380, 400, 390],
  "duration4": [50, 40, 45, 50, 50, 45],
  "test4":[12, 16, 15, 16, 15, 19],
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
# TimeX = df["Time"]
# print(DataQ)
# # print(df)
# st.line_chart(DataQ ,x=DataQ.index)
st.set_page_config(layout="wide")



with open('TestFolder/Test.css') as f: # Test.css with command prompt : TestFolder/Test.css with PowerShell
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# st.line_chart(df["calories"])
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("data1","data2" )
)

if "data1" in add_selectbox: # If user selects Email  do 👇
    data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')
    Ex = data.reset_index(drop=True)
else:
    data1 = pd.read_csv('Component/Data/Dataset/All134.csv')
    Ex = data1.reset_index(drop=True)

st.markdown("# :green[Anomaly Detection Dashborad] ")
st.markdown("#")
def Test(Ex):
    col1, col2 = st.columns((30,30))
    with col1:
        st.header("Line Chart")
        st.line_chart(df["calories"])
        # st.line_chart(Ex1["RD81DL96_1"])
    with col2:
        st.header("Dataframe")
        # st.dataframe(df)
        st.dataframe(Ex)

    col3, col4 = st.columns(2)
    with col3:  
        fig = px.line(df, x = 'test',y = df.columns[:-1])
        st.plotly_chart(fig,use_container_width=True, sharing="streamlit", theme="streamlit")  
    with col4:
        Prediction1 = len(df[df['calories']==400])
        Prediction_1 = len(df[df['duration']==50])
        piechart = [Prediction1,Prediction_1]
        detection = ['Normally','Anomaly']
        fig = px.pie(values=piechart,names=detection)

        st.header("Pie Chart")
        st.plotly_chart(fig, use_container_width=True)

# Start = st.button("Click here to start")
# if Start:
#     Test(Ex)
Test(Ex)

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )
# col2.markdown(
#     """
#     <style>
#     .st-b8 {
#         border: 2px solid black;
#         padding: 10px;
#         border-radius: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# col1.markdown(
#     """
#     <style>
#     .st-b9 {
#         border: 2px solid black;
#         padding: 10px;
#         border-radius: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
        
