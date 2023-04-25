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
# DataQ = DataQ.set_index('Time')
# Test = df[["Prediction","Probability","Std3"]]
fig = px.line(DataQ, x='Time',y=DataQ.columns[:-1])
# TimeX = df["Time"]
# print(DataQ)
# # print(df)
# st.line_chart(DataQ ,x=DataQ.index)
st.dataframe(DataQ)
st.plotly_chart(fig)

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3), 
#     columns=["a", "b", "c"])
# print(chart_data)

# import streamlit as st
# from vega_datasets import data

# source = data.cars()
# print(source)
# def Run():

#         firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
#         result = firebaseDB.get('/FinalProject', '')
#         vals = list(result.values())
#         # df = pd.DataFrame()
#         print(len(vals))

# Run()
# # Function to listen for changes in the Firebase database
# def listen():
#     while True:
#         data = ref.get()
#         show_data(data)

# # Main function
# def main():
#     st.title("Real-time dashboard")

#     # Start listening for changes in the Firebase database
#     listen()

# if __name__ == '__main__':
#     main()

# print(result)

# df = pd.DataFrame()

# for KeyName in result:
#     # print(result[KeyName]["Prediction"],result[KeyName]["Probability"],result[KeyName]["Result"],result[KeyName]["Time"])
#     # print(result[KeyName])
#     Prediction = result[KeyName]["Prediction"]
#     Probability = result[KeyName]["Probability"]
#     Result = result[KeyName]["Result"]
#     Time = result[KeyName]["Time"]

#     # print(Prediction,Probability,Result,Time)
#     Data = {"Prediction":[Prediction],"Probability":[Probability],
#             "Result":[Result],"Time":[Time]}
#     # print(Data)
#     Data = pd.DataFrame(Data)
#     df = pd.concat([df, Data], axis=0)

# df = df.reset_index(drop=True)
# # print(df.reset_index(drop=True))
# DataQ = df["Prediction"]
# print(DataQ)
# data = pd.read_csv('Data/Dataset/TotalFile35_36.csv')
# ForTest = data
# ForTest = ForTest["level_2"].head(10)
# DataQ = pd.DataFrame(ForTest)
# print(DataQ.reset_index(drop=True))



# def get_live_feed_data():
#     return random.randint(0, 100)
# # Connect to your live feed source and get the data

# placeholder = st.empty()
# live_feed_data = get_live_feed_data()

# # Create the Streamlit app
# # st.title('Live Feed Dashboard')
# # st.write('Here is some live feed data:')
# # st.write(live_feed_data)

# # Set up a loop to update the data

# for seconds in range(10):
#     # with placeholder.container():    
#         new_data = get_live_feed_data()
        
#         if new_data != live_feed_data:
                
#                 ive_feed_data = new_data
#                 # 
#                 st.write('New data received:')
#                 st.write(live_feed_data)

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
# st.button("Re-run")
# import multiprocessing

# def child_process():
#     print("This is a child process.")

# def parent_process():
#     print("This is a parent process.")
#     daemon_process = multiprocessing.Process(target=child_process)
#     daemon_process.daemon = False
#     daemon_process.start()

# if __name__ == '__main__':
#     parent_process()