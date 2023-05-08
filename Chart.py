from firebase import firebase
import plotly.express as px
import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

def Run(IfNotUseDatabase,Name_for_database):
    # print("Chart")

    df = pd.DataFrame()

    # From database
    firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
    result = firebaseDB.get('/{}'.format(Name_for_database), '')
    # result = firebaseDB.get('/FinalProject', '')
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
    # print(df)
    DataQ = df[["Prediction","Probability","Std3","Std2","Mean2","Std1","PToP1","PToP4","PToP2","Std4","Kurtosis1","Kurtosis4","Time"]]

    # If want Data from dataframe
    # DataQ = IfNotUseDatabase[["Prediction","Probability","Std3","Std2","Mean2","Std1","PToP1","PToP4","PToP2","Std4","Kurtosis1","Kurtosis4","Time"]]

    # CSS
    with open('Style.css') as f: # Test.css with command prompt : TestFolder/Test.css with PowerShell
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Make Realtime Streamlit
    tab1, tab2, tab3 = st.tabs(["📈 Dashboard", "📑 Data", "⚙️ Setting"])
    with tab2:
        
        col1, col2, col3 = st.columns((60,5,20))
        with col1:
            st.header("Dataframe")
            st.dataframe(DataQ)
        with col2:
            st.write("")
        with col3:
            st.header("Result")
            st.dataframe(df["Result"])

    with tab1:
        st.markdown("# :black[Anomaly Detection Dashborad] ")
        st.markdown("#")

        col1, col2 = st.columns((30,30))
        with col1:
            st.header("Line Chart")
            st.line_chart(DataQ["Prediction"])
        with col2:
            Prediction1 = len(DataQ[DataQ['Prediction']==1])
            Prediction_1 = len(DataQ[DataQ['Prediction']==-1])
            piechart = [Prediction1,Prediction_1]
            detection = ['Normally','Anomaly']
            fig = px.pie(values=piechart,names=detection)
            st.header("Pie Chart")
            st.plotly_chart(fig, use_container_width=True)

        col2, col3 = st.columns((30,30))
        with col2:
            fig = px.line(DataQ, x = 'Time',y = DataQ.columns[2:-6])
            st.plotly_chart(fig, use_container_width=True)
        with col3:
            fig = px.line(DataQ, x = 'Time',y = DataQ.columns[7:-1])
            st.plotly_chart(fig, use_container_width=True)


    return DataQ

        
        
 