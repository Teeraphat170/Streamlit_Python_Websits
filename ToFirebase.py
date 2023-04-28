from firebase import firebase
import time
import warnings
warnings.filterwarnings("ignore")

def ToFirebase(okng,timeX,prediction_proba,prediction,Std3,Std2,Mean2,Std1,PToP1,PToP4,PToP2,Std4,Kurtosis1,Kurtosis4):
    firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)

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
            'Result':okng,
            'Time':timeX,
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

