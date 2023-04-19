import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from datetime import datetime

def predict(TestX):
    time = datetime.today().strftime('%H:%M:%S')
    # filename = filename
    df = TestX
    # print(df)

    #unsupervised IsolationForest
    load_clf = pickle.load(open("Model/IsolationForest_7.pkl", "rb")) #---------------------ใช้อันนี้เป็นหลัก---------------------#

    # IsolationForest
    prediction = load_clf.predict(df) 
    prediction_proba = load_clf.decision_function(df)

    if prediction[0] == 0 and prediction_proba[0][0] > 0.51:
        OKNG = 'NG'
        # OKNG = 'OK'
    else:
        OKNG = 'OK'
        # OKNG = 'NG'

    return OKNG,time,prediction_proba,prediction 

