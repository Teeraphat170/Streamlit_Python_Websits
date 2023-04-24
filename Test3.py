import numpy as np
import pandas as pd
import statistics
import time as T
import warnings
import streamlit as st
from scipy.stats import kurtosis
from firebase import firebase
import pickle
from datetime import datetime
warnings.filterwarnings("ignore")

# data = pd.read_csv('Data/Dataset/All134.csv')
data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')

# Main
def ReadCSV(df):
    TestX = df
    TestX = TestX.iloc[: , 1:] 

    firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
    firebaseDB.delete('/FinalProject','')

    placeholder = st.empty()
    First,Last = 0,390
    while Last <= len(TestX): 
        Position = TestX.iloc[First:Last]
        scaled_newdf = Position
        Mean = pd.DataFrame()
        for x in scaled_newdf:
            total = scaled_newdf[x].mean()
            df2 = pd.DataFrame([total])
            Mean = pd.concat([Mean, df2], axis=1)
        Mean.columns = ['Mean1','Mean2','Mean3','Mean4','Mean5','Mean6','Mean7','Mean8','Mean9']
        Median = pd.DataFrame()
        for x in scaled_newdf:
            total = scaled_newdf[x].median()
            df2 = pd.DataFrame([total])
            Median = pd.concat([Median, df2], axis=1)
        Median.columns = ['Median1','Median2','Median3','Median4','Median5','Median6','Median7','Median8','Median9']
        Std = pd.DataFrame()
        for x in scaled_newdf:
            total = scaled_newdf[x].std()
            df2 = pd.DataFrame([total])
            Std = pd.concat([Std, df2], axis=1)
        Std.columns = ['Std1','Std2','Std3','Std4','Std5','Std6','Std7','Std8','Std9']
        Mode = pd.DataFrame()
        for x in scaled_newdf:
            total = statistics.mode(scaled_newdf[x])
            df2 = pd.DataFrame([total])
            Mode = pd.concat([Mode, df2], axis=1)
        Mode.columns = ['Mode1','Mode2','Mode3','Mode4','Mode5','Mode6','Mode7','Mode8','Mode9']
        Kurt = pd.DataFrame()
        for x in scaled_newdf:
            total = kurtosis(scaled_newdf[x],bias=False)
            df2 = pd.DataFrame([total])
            Kurt = pd.concat([Kurt, df2], axis=1)
        Kurt.columns = ['Kurtosis1','Kurtosis2','Kurtosis3','Kurtosis4','Kurtosis5','Kurtosis6','Kurtosis7','Kurtosis8','Kurtosis9'] # New way
        PtoP = pd.DataFrame()
        for x in scaled_newdf:
            total = scaled_newdf[x].max() + scaled_newdf[x].min()
            df2 = pd.DataFrame([total])
            PtoP = pd.concat([PtoP, df2], axis=1)
        PtoP.columns = ['PToP1','PToP2','PToP3','PToP4','PToP5','PToP6','PToP7','PToP8','PToP9']
        RMS = pd.DataFrame() 
        for x in scaled_newdf:
            c = TestX[x]
            da1 = c.iloc[[0]]
            total = np.sqrt((da1**2).sum() / len(scaled_newdf[x]))
            df2 = pd.DataFrame([total])
            RMS = pd.concat([RMS, df2], axis=1)
        RMS.columns = ['RMS1','RMS2','RMS3','RMS4','RMS5','RMS6','RMS7','RMS8','RMS9']

        result = pd.concat([Mean, Median], axis=1)
        result = pd.concat([result, Std], axis=1)
        result = pd.concat([result, Mode], axis=1)
        result = pd.concat([result, Kurt], axis=1)
        result = pd.concat([result, PtoP], axis=1)
        result = pd.concat([result, RMS], axis=1)
        newresult = result[['Std3','Std2','Mean2','Std1','PToP1','PToP4','PToP2','Std4','Kurtosis1','Kurtosis4']]

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

        # predict
        time = datetime.today().strftime('%H:%M:%S')
        df = newresult

        load_clf = pickle.load(open('Component/Data/Model/IsolationForest_7.pkl', 'rb')) 

        prediction = load_clf.predict(df) 
        prediction_proba = load_clf.decision_function(df)

        if prediction[0] == -1 and prediction_proba[0] < 0:
            OKNG = 'NG'
        else:
            OKNG = 'OK'

        # ToFirebase
        prediction_proba = prediction_proba[0]
        prediction_proba = round(prediction_proba,2)

        prediction = prediction[0]
        prediction = float(prediction)

        Std3 = float(Std3)
        Std3 = round(Std3,2)

        Std2 = float(Std2)
        Std2 = round(Std2,2)

        Mean2 = float(Mean2)
        Mean2 = round(Mean2,2)

        Std1 = float(Std1)
        Std1 = round(Std1,2)

        PToP1 = float(PToP1)
        PToP1 = round(PToP1,2)

        PToP4 = float(PToP4)
        PToP4 = round(PToP4,2)

        PToP2 = float(PToP2)
        PToP2 = round(PToP2,2)

        Std4 = float(Std4)
        Std4 = round(Std4,2)

        Kurtosis1 = float(Kurtosis1)
        Kurtosis1 = round(Kurtosis1,2)

        Kurtosis4 = float(Kurtosis4)
        Kurtosis4 = round(Kurtosis4,2)

        data = {
                'Result':OKNG,
                'Time':time,
                'Prediction':prediction,
                'Probability':prediction_proba,
                'Std3':Std3,
                'Std2':Std2,
                'Mean2':Mean2,
                'Std1':Std1,
                'PToP1':PToP1,
                'PToP4':PToP4,
                'PToP2':PToP2,
                'Std4':Std4,
                'Kurtosis1':Kurtosis1,
                'Kurtosis4':Kurtosis4,
            }

        # time.sleep(1)

        firebaseDB.post('/FinalProject',data)
        
        
        with placeholder.container():
            # T.sleep(2)
            # try:
            df = pd.DataFrame()
            firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
            result = firebaseDB.get('/FinalProject', '')

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
            print(df)
            st.dataframe(df)
            DataQ = df["Prediction"]

                    # Make Realtime
        # listForRealtime = []
        # i = 1
        # while i < len(df.index) + 1:
        #     listForRealtime.append(i)
        #     i = i + 1
        #     X = pd.DataFrame(listForRealtime,columns = ['X-axis'])
        # result = pd.concat([X, DataQ], axis=1)

        # st.line_chart(result, x='X-axis')
                # st.dataframe(df)
            # except:
                # pass

        First = First + 5
        Last = Last + 5

    # return okng,timeX,prediction_proba,prediction
ReadCSV(data)