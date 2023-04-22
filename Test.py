from firebase import firebase
import pandas as pd

# firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
# # result = firebaseDB.get('/FinalProject', '')
# firebaseDB.delete('/FinalProject','')
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

import streamlit as st
import random

def get_live_feed_data():
    return random.randint(0, 100)
# Connect to your live feed source and get the data

placeholder = st.empty()
live_feed_data = get_live_feed_data()

# Create the Streamlit app
st.title('Live Feed Dashboard')
st.write('Here is some live feed data:')
st.write(live_feed_data)

# Set up a loop to update the data
with placeholder.container():
    while True:
        new_data = get_live_feed_data()
        if new_data != live_feed_data:
            live_feed_data = new_data
            st.write('New data received:')
            st.write(live_feed_data)