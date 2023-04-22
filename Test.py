from firebase import firebase
import pandas as pd

firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
result = firebaseDB.get('/FinalProject', '')
# print(result)

df = pd.DataFrame()

for KeyName in result:
    # print(result[KeyName]["Prediction"],result[KeyName]["Probability"],result[KeyName]["Result"],result[KeyName]["Time"])
    # print(result[KeyName])
    Prediction = result[KeyName]["Prediction"]
    Probability = result[KeyName]["Probability"]
    Result = result[KeyName]["Result"]
    Time = result[KeyName]["Time"]

    # print(Prediction,Probability,Result,Time)
    Data = {"Prediction":[Prediction],"Probability":[Probability],
            "Result":[Result],"Time":[Time]}
    # print(Data)
    Data = pd.DataFrame(Data)
    df = pd.concat([df, Data], axis=0)

df = df.reset_index(drop=True)
# print(df.reset_index(drop=True))
DataQ = df["Prediction"]
print(DataQ)
# data = pd.read_csv('Data/Dataset/TotalFile35_36.csv')
# ForTest = data
# ForTest = ForTest["level_2"].head(10)
# DataQ = pd.DataFrame(ForTest)
# print(DataQ.reset_index(drop=True))

