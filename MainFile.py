import numpy as np
import pandas as pd
import statistics
import time
import warnings
import streamlit as st
import pickle
from datetime import datetime
from scipy.stats import kurtosis
from firebase import firebase
from Predict import predict
from ToFirebase import ToFirebase
from Chart import Run
warnings.filterwarnings("ignore")

# data = pd.read_csv('Data/Dataset/All134.csv')
# data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')

# Main
def MainProcess(df):
    # print("Calculate")
    TestX = df
    # TestX = TestX.iloc[: , 1:] 
    TestX = TestX.iloc[: , 1:5]
    
    # count Time
    start = time.time()

    # Set for 1 container
    placeholder = st.empty()

    # Add new
    IfNotUseDatabase = pd.DataFrame()

    ###### Sliding Windows
    First,Last = 0,390

    while Last <= len(TestX): 
   
        Position = TestX.iloc[First:Last]

        # If not use scale data
        scaled_newdf = Position

        Mean = pd.DataFrame()
        for x in scaled_newdf:
            total = scaled_newdf[x].mean()
            df2 = pd.DataFrame([total])
            Mean = pd.concat([Mean, df2], axis=1)

        Mean.columns = ['Mean1','Mean2','Mean3','Mean4']
        # Mean.columns = ['Mean1','Mean2','Mean3','Mean4','Mean5',
        #                 'Mean6','Mean7','Mean8','Mean9']


        Median = pd.DataFrame()
        for x in scaled_newdf:
            total = scaled_newdf[x].median()
            df2 = pd.DataFrame([total])
            Median = pd.concat([Median, df2], axis=1)

        Median.columns = ['Median1','Median2','Median3','Median4']
        # Median.columns = ['Median1','Median2','Median3','Median4','Median5',
        #                   'Median6','Median7','Median8','Median9']

        Std = pd.DataFrame()
        for x in scaled_newdf:
        # for x in TestX:
            total = scaled_newdf[x].std()
            df2 = pd.DataFrame([total])
            Std = pd.concat([Std, df2], axis=1)

        Std.columns = ['Std1','Std2','Std3','Std4']
        # Std.columns = ['Std1','Std2','Std3','Std4',
        #                'Std5','Std6','Std7','Std8','Std9']

        Mode = pd.DataFrame()
        for x in scaled_newdf:
            total = statistics.mode(scaled_newdf[x])
            df2 = pd.DataFrame([total])
            Mode = pd.concat([Mode, df2], axis=1)

        Mode.columns = ['Mode1','Mode2','Mode3','Mode4']
        # Mode.columns = ['Mode1','Mode2','Mode3','Mode4','Mode5',
        #                 'Mode6','Mode7','Mode8','Mode9']

        Kurt = pd.DataFrame()
        for x in scaled_newdf:

            total = kurtosis(scaled_newdf[x],bias=False)
            df2 = pd.DataFrame([total])
            Kurt = pd.concat([Kurt, df2], axis=1)

        Kurt.columns = ['Kurtosis1','Kurtosis2','Kurtosis3',
                        'Kurtosis4']
        # Kurt.columns = ['Kurtosis1','Kurtosis2','Kurtosis3',
        #                 'Kurtosis4','Kurtosis5','Kurtosis6',
        #                 'Kurtosis7','Kurtosis8','Kurtosis9']

        PtoP = pd.DataFrame()
        for x in scaled_newdf:

            total = scaled_newdf[x].max() + scaled_newdf[x].min()
            df2 = pd.DataFrame([total])
            PtoP = pd.concat([PtoP, df2], axis=1)

        PtoP.columns = ['PToP1','PToP2','PToP3','PToP4']
        # PtoP.columns = ['PToP1','PToP2','PToP3','PToP4',
        #                 'PToP5','PToP6','PToP7','PToP8','PToP9']

        RMS = pd.DataFrame() 
        for x in scaled_newdf:

            c = TestX[x]
            da1 = c.iloc[[0]]
            total = np.sqrt((da1**2).sum() / len(scaled_newdf[x]))
            df2 = pd.DataFrame([total])
            RMS = pd.concat([RMS, df2], axis=1)

        RMS.columns = ['RMS1','RMS2','RMS3','RMS4']
        # RMS.columns = ['RMS1','RMS2','RMS3','RMS4',
        #                'RMS5','RMS6','RMS7','RMS8','RMS9']
        # print(RMS)

        result = pd.concat([Mean, Median], axis=1)
        result = pd.concat([result, Std], axis=1)
        result = pd.concat([result, Mode], axis=1)
        result = pd.concat([result, Kurt], axis=1)
        result = pd.concat([result, PtoP], axis=1)
        result = pd.concat([result, RMS], axis=1)

        
        newresult = result[['Std3','Std2','Mean2','Std1','PToP1','PToP4','PToP2','Std4','Kurtosis1','Kurtosis4']]
        # print(newresult)

        Std3 = newresult.get("Std3")
        Std2 = newresult.get("Std2")
        Mean2 = newresult.get("Mean2")
        Std1 = newresult.get("Std1")
        PToP1 = newresult.get("PToP1")
        PToP4 = newresult.get("PToP4")
        PToP2 = newresult.get("PToP2")
        Std4 = newresult.get("Std4")
        Kurtosis1 = newresult.get("Kurtosis1")
        Kurtosis4 = newresult.get("Kurtosis4")


        # To predict
        OKNG,timeX,prediction_proba,prediction = predict(newresult) #Supervised And IsolationForest
        # print(OKNG,timeX,prediction_proba,prediction)

        # If_Not_use_database
        data = {
            "Result": [OKNG],
            "Time": [timeX],
            "Probability": [prediction_proba][0],
            "Prediction": [prediction][0],
            }
        result_for_predict = pd.DataFrame(data)
        result_for_predict = pd.concat([result_for_predict, newresult], axis=1)
        IfNotUseDatabase = pd.concat([IfNotUseDatabase,result_for_predict], axis=0)
        IfNotUseDatabase = IfNotUseDatabase.reset_index(drop=True)
        # print(IfNotUseDatabase)

        #if wanna see Result
        # print(okng,timeX,prediction_proba[0],prediction[0],Std3,Std2,Mean2,Std1,PToP1,PToP4,PToP2,Std4,Kurtosis1,Kurtosis4) 

        # ToFirebase
        # ToFirebase(OKNG,timeX,prediction_proba,prediction,Std3,Std2,
        #            Mean2,Std1,PToP1,PToP4,PToP2,Std4,Kurtosis1,Kurtosis4,)
          
        with placeholder.container():
            Run(IfNotUseDatabase)
            # Run()

        First = First + 10 # or + 5
        Last = Last + 10 # or + 5
        # end = time.time()
        # print("Time use : ",end - start)
    return OKNG,timeX,prediction_proba,prediction

def WTF(data):
    # Clear Database for New Run 
    # firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
    # firebaseDB.delete('/FinalProject','')

    # print("Start")
    MainProcess(data)


# For Test
# st.set_page_config(layout="wide")
# Start = st.button("Click here to start")
# if Start:
#     WTF()

# WTF()