from firebase import firebase
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def ToFirebase(dataframe):
    firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)

    json = dataframe.to_json(orient = 'columns')
    # prediction_proba = prediction_proba[0]
    # prediction_proba = round(prediction_proba,2)

    # prediction = prediction[0]
    # prediction = float(prediction)

    # Std3 = float(Std3)
    # Std3 = round(Std3,2)

    # Std2 = float(Std2)
    # Std2 = round(Std2,2)

    # Mean2 = float(Mean2)
    # Mean2 = round(Mean2,2)

    # Std1 = float(Std1)
    # Std1 = round(Std1,2)

    # PToP1 = float(PToP1)
    # PToP1 = round(PToP1,2)

    # PToP4 = float(PToP4)
    # PToP4 = round(PToP4,2)

    # PToP2 = float(PToP2)
    # PToP2 = round(PToP2,2)

    # Std4 = float(Std4)
    # Std4 = round(Std4,2)

    # Kurtosis1 = float(Kurtosis1)
    # Kurtosis1 = round(Kurtosis1,2)

    # Kurtosis4 = float(Kurtosis4)
    # Kurtosis4 = round(Kurtosis4,2)


    # # SendtodataBase
    data = {
            'Result':dataframe["Result"].to_list(),
            'Time':dataframe["Time"].to_list(),
            'Prediction':dataframe["Prediction"].to_list(),
            'Probability':dataframe["Probability"].to_list(),
            'Std3':dataframe["Std3"].to_list(),
            'Std2':dataframe["Std2"].to_list(),
            'Mean2':dataframe["Mean2"].to_list(),
            'Std1':dataframe["Std1"].to_list(),
            'PToP1':dataframe["PToP1"].to_list(),
            'PToP4':dataframe["PToP4"].to_list(),
            'PToP2':dataframe["PToP2"].to_list(),
            'Std4':dataframe["Std4"].to_list(),
            'Kurtosis1':dataframe["Kurtosis1"].to_list(),
            'Kurtosis4':dataframe["Kurtosis4"].to_list(),
        }
    # print(data)
    # firebaseDB.post('/{}'.format(Name_for_database),data)
    firebaseDB.post('/FinalProject',data)
    # print(data)

