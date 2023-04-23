from datetime import datetime
from scipy.stats import kurtosis
from MainFile import ReadCSV
from threading import Thread
from firebase import firebase
from firebase_admin import credentials
from firebase_admin import db
# import ray
import firebase_admin
import threading
import multiprocessing
import multiprocessing.pool
import time
import pickle
import streamlit as st
import statistics
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
# import warnings
# warnings.filterwarnings("ignore")
data = pd.read_csv('Data/Dataset/TotalFile35_36.csv')

# def Run():
#     placeholder = st.empty()

#     # Retrieving The Data
#     for seconds in range(100):
#         firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
#         result = firebaseDB.get('/FinalProject', '')

#         df = pd.DataFrame()

#         for KeyName in result:
#             Prediction = result[KeyName]["Prediction"]
#             Probability = result[KeyName]["Probability"]
#             Result = result[KeyName]["Result"]
#             Time = result[KeyName]["Time"]

#             # print(Prediction,Probability,Result,Time)
#             Data = {"Prediction":[Prediction],"Probability":[Probability],
#                 "Result":[Result],"Time":[Time]}
#             # print(Data)
#             Data = pd.DataFrame(Data)
#             df = pd.concat([df, Data], axis=0)

#         df = df.reset_index(drop=True)
#         DataQ = df["Prediction"]

#         # Make Realtime
#         list = []
#         i = 0
#         while i < len(df.index):
#             i = i + 1
#             list.append(i)
#             X = pd.DataFrame(list,columns = ['X-axis'])
#         result = pd.concat([X, DataQ], axis=1)
#         # print(result)

#         with placeholder.container():

#             st.line_chart(result, x='X-axis')
#             time.sleep(1)

# # # Run()

# def Main():
#     ReadCSV(data)


def tt():
    time = datetime.today().strftime('%H:%M:%S')
    print("test1",time)

def ttt():
    time = datetime.today().strftime('%H:%M:%S')
    print("test2",time)

def GGG():
    # p2 = multiprocessing.Process(target=Run)
    # p1 = multiprocessing.Process(target=Main)

    p1 = multiprocessing.Process(target = tt)
    p2 = multiprocessing.Process(target = ttt)
    
    p1.start()
    time.sleep(5)
    p2.start()
    # p1.join()
    # p2.join()

if __name__ == '__main__':
    GGG()















