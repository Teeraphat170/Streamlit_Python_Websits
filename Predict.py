import pickle
from datetime import datetime
from sklearn.ensemble import IsolationForest



def predict(TestX):
    # print("Predict")
    time = datetime.today().strftime('%H:%M:%S')
    df = TestX

    load_clf = pickle.load(open('Component/Data/Model/IsolationForest_7.pkl', 'rb')) 
    # load_clf = pickle.load(open('Component/Data/Model/IsolationForest_9.pkl', 'rb')) 


    # IsolationForest
    prediction = load_clf.predict(df) 
    prediction_proba = load_clf.decision_function(df)

    if prediction[0] == -1 and prediction_proba[0] < 0:
        OKNG = 'NG'
        # OKNG = 'OK'
    else:
        OKNG = 'OK'
        # OKNG = 'NG'

    
    return OKNG,time,prediction_proba,prediction 

