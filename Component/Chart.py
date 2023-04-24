from firebase import firebase
import pandas as pd
import time
import streamlit as st
import pandas as pd
import time
import warnings
warnings.filterwarnings("ignore")


def Run():
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
    DataQ = df["Prediction"]

    # Make Realtime
    col2, col3 = st.columns((30,30))
    with col2:
        st.line_chart(DataQ)
    with col3:
        st.dataframe(df)

        
        
 