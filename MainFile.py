import numpy as np
import pandas as pd
# from Predict import predict
import statistics
import pickle
from datetime import datetime
from scipy.stats import kurtosis
from firebase import firebase
import warnings
warnings.filterwarnings("ignore")

# data = pd.read_csv('Data/Dataset/All134.csv')
data = pd.read_csv('Data/Dataset/TotalFile35_36.csv')


# Main
def ReadCSV(df):
    TestX = df
    TestX = TestX.iloc[: , 1:] 

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

        Mean.columns = ['Mean1','Mean2','Mean3','Mean4','Mean5',
                        'Mean6','Mean7','Mean8','Mean9']
        # print(Mean)

        Median = pd.DataFrame()
        for x in scaled_newdf:
            total = scaled_newdf[x].median()
            df2 = pd.DataFrame([total])
            Median = pd.concat([Median, df2], axis=1)

        Median.columns = ['Median1','Median2','Median3','Median4','Median5',
                          'Median6','Median7','Median8','Median9']
        # print(Median)

        Std = pd.DataFrame()
        for x in scaled_newdf:
        # for x in TestX:
            total = scaled_newdf[x].std()
            df2 = pd.DataFrame([total])
            Std = pd.concat([Std, df2], axis=1)

        Std.columns = ['Std1','Std2','Std3','Std4',
                       'Std5','Std6','Std7','Std8','Std9']
        # print(Std)

        Mode = pd.DataFrame()
        for x in scaled_newdf:
            total = statistics.mode(scaled_newdf[x])
            df2 = pd.DataFrame([total])
            Mode = pd.concat([Mode, df2], axis=1)

        Mode.columns = ['Mode1','Mode2','Mode3','Mode4','Mode5',
                        'Mode6','Mode7','Mode8','Mode9']
        # print(Mode)

        Kurt = pd.DataFrame()
        for x in scaled_newdf:

            total = kurtosis(scaled_newdf[x],bias=False)
            df2 = pd.DataFrame([total])
            Kurt = pd.concat([Kurt, df2], axis=1)

        Kurt.columns = ['Kurtosis1','Kurtosis2','Kurtosis3',
                        'Kurtosis4','Kurtosis5','Kurtosis6',
                        'Kurtosis7','Kurtosis8','Kurtosis9'] # New way
        # print(Kurt)

        PtoP = pd.DataFrame()
        for x in scaled_newdf:

            total = scaled_newdf[x].max() + scaled_newdf[x].min()
            df2 = pd.DataFrame([total])
            PtoP = pd.concat([PtoP, df2], axis=1)

        PtoP.columns = ['PToP1','PToP2','PToP3','PToP4',
                        'PToP5','PToP6','PToP7','PToP8','PToP9']
        # print(PtoP)

        RMS = pd.DataFrame() 
        for x in scaled_newdf:

            c = TestX[x]
            da1 = c.iloc[[0]]
            total = np.sqrt((da1**2).sum() / len(scaled_newdf[x]))
            df2 = pd.DataFrame([total])
            RMS = pd.concat([RMS, df2], axis=1)

        RMS.columns = ['RMS1','RMS2','RMS3','RMS4',
                       'RMS5','RMS6','RMS7','RMS8','RMS9']
        # print(RMS)

        result = pd.concat([Mean, Median], axis=1)
        result = pd.concat([result, Std], axis=1)
        result = pd.concat([result, Mode], axis=1)
        result = pd.concat([result, Kurt], axis=1)
        result = pd.concat([result, PtoP], axis=1)
        result = pd.concat([result, RMS], axis=1)

        # print(newresult)
        newresult = result[['Std3','Std2','Mean2','Std1','PToP1','PToP4','PToP2','Std4','Kurtosis1','Kurtosis4']]

        okng,timeX,prediction_proba,prediction = predict(newresult) #Supervised And IsolationForest

        #if wanna see Result
        # print(First,Last,okng,timeX,prediction_proba[0],prediction[0]) 

        # ToFirebase
        vdv = ToFirebase(okng,timeX,prediction_proba,prediction)

        First = First + 5
        Last = Last + 5

    return okng,timeX,prediction_proba,prediction

# Prediction
def predict(TestX):
    time = datetime.today().strftime('%H:%M:%S')
    df = TestX

    load_clf = pickle.load(open('Data/Model/IsolationForest_7.pkl', 'rb')) 

    # IsolationForest
    prediction = load_clf.predict(df) 
    prediction_proba = load_clf.decision_function(df)
    # print(prediction_proba)

    if prediction[0] == -1 and prediction_proba[0] < 0:
        OKNG = 'NG'
        # OKNG = 'OK'
    else:
        OKNG = 'OK'
        # OKNG = 'NG'

    return OKNG,time,prediction_proba,prediction 


# ToFirebase
def ToFirebase(okng,timeX,prediction_proba,prediction):
    
    firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)

    prediction_proba = prediction_proba[0]
    prediction_proba = round(prediction_proba,2)

    prediction = prediction[0]
    prediction = float(prediction)

    data = {
            'Result':okng,
            'Time':timeX,
            'Prediction':prediction,
            'Probability':prediction_proba
        }

    result = firebaseDB.post('/FinalProject',data)
    return result

okng,timeX,prediction_proba,prediction = ReadCSV(data)