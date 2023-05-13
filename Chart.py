from firebase import firebase
import time
import random
import string
import plotly.express as px
import pandas as pd
import streamlit as st
import warnings
warnings.filterwarnings("ignore")

def Run(IfNotUseDatabase,Data_From_Database,options1):
    # print("Chart")

    df = pd.DataFrame()

    # From database
    # firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
    # result = firebaseDB.get('/{}'.format(Name_for_database), '')
    # # result = firebaseDB.get('/FinalProject', '')
    # for key, value in result.items():
    #     Prediction = value["Prediction"]
    #     Probability = value["Probability"]
    #     Result = value["Result"]
    #     Time = value["Time"]
    #     Std3 = value["Std3"]
    #     Std2 = value["Std2"]
    #     Mean2 = value["Mean2"]
    #     Std1 = value["Std1"]
    #     PToP1 = value["PToP1"]
    #     PToP4 = value["PToP4"]
    #     PToP2 = value["PToP2"]
    #     Std4 = value["Std4"]
    #     Kurtosis1 = value["Kurtosis1"]
    #     Kurtosis4 = value["Kurtosis4"]

    #     Data = {"Prediction":[Prediction],"Probability":[Probability],"Result":[Result],"Time":[Time],"Std3":[Std3],
    #                 "Std2":[Std2],"Mean2":[Mean2],"Std1":[Std1],"PToP1":[PToP1],"PToP4":[PToP4],
    #                 "PToP2":[PToP2],"Std4":[Std4],"Kurtosis1":[Kurtosis1],"Kurtosis4":[Kurtosis4],}
            
    #     Data = pd.DataFrame(Data)
    #     df = pd.concat([df, Data], axis=0)

    # df = df.reset_index(drop=True)
    # # print(df)
    # DataQ = df[["Prediction","Probability","Std3","Std2","Mean2","Std1","PToP1","PToP4","PToP2","Std4","Kurtosis1","Kurtosis4","Time"]]
    try:
        Data_From_Database = Data_From_Database[["Prediction","Probability","Std3","Std2","Mean2","Std1","PToP1","PToP4","PToP2","Std4","Kurtosis1","Kurtosis4","Time"]]
    except:
        pass

    DataQ = IfNotUseDatabase[["Prediction","Probability","Std3","Std2","Mean2","Std1","PToP1","PToP4","PToP2","Std4","Kurtosis1","Kurtosis4","Time"]]
    

    DataQ = pd.concat([Data_From_Database,DataQ],axis=0)
    DataQ = DataQ.reset_index(drop=True)
    # st.dataframe(DataQ["Prediction"])
    # CSS
    
    with open('Style.css') as f: # Test.css with command prompt : TestFolder/Test.css with PowerShell
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    # Make Realtime Streamlit
    # tab1, tab2, tab3 = st.tabs(["📈 Dashboard", "📑 Data", "⚙️ Setting"])
    tab1, tab2 = st.tabs(["📈 Dashboard", "📑 Data"])
    with tab2:
        col1, col2, col3 = st.columns((4,10,1))
        with col2:
            st.header("Statistical Value")
            st.dataframe(DataQ[["Std3","Std2","Mean2","Std1","PToP1","PToP4","PToP2","Std4","Kurtosis1","Kurtosis4"]])
        with col1:
            st.header("Result")
            st.dataframe(DataQ[["Prediction","Probability","Time"]])
    
    with tab1:
        st.markdown("# :black[Anomaly Detection Dashborad] ")
        # st.markdown("Anomaly Detection Dashborad")
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
            st.header("Line Chart")
            for_line_chart1 = pd.DataFrame()
            # Data1 = DataQ[["Std3","Std2","Mean2","Std1","PToP1","Time"]]
            for x in options1:
                # FFF.append(DataQ[x])
                for_line_chart1 = pd.concat([for_line_chart1,DataQ[x]], axis=1)
                # print(DataQ[x])

            Data1 = pd.concat([for_line_chart1,DataQ["Time"]], axis=1)
            # Data1 = DataQ[["Std3","Std2","Mean2","Std1","PToP1","Time"]]
            st.line_chart(Data1, x = 'Time')

            # fig = px.line(DataQ, x = 'Time',y = DataQ.columns[2:-6])
            # st.plotly_chart(fig, use_container_width=True)

        with col3: 
            # start = time.time()
            st.header("Line Chart")
            # fig = px.line(DataQ, x = 'Time',y = DataQ.columns[7:-1])
            # st.plotly_chart(fig, use_container_width=True)

            Data2 = DataQ[["PToP4","PToP2","Std4","Kurtosis1","Kurtosis4","Time"]]
            st.line_chart(Data2, x = 'Time')

            # end = time.time()
            # print("Time use Chart: ",end - start)

  
            
    # Stop = st.button('Stop Running', use_container_width=False,key=DataQ['Prediction'][0])
    return DataQ
        
        
# start = time.time()
# end = time.time()
# print("Time use in Chart: ",end - start)
        
        
 