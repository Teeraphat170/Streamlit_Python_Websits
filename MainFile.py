import numpy as np
import pandas as pd
import statistics
import time
import warnings
import streamlit as st
import pickle
import plotly.express as px
import string
import random
from PIL import Image
from datetime import datetime
from scipy.stats import kurtosis
from firebase import firebase
from Predict import predict
from ToFirebase import ToFirebase
from Chart import Run
warnings.filterwarnings("ignore")

# data = pd.read_csv('Data/Dataset/All134.csv')
# data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')

# Main
def MainProcess(df,Row,dataframe):
    # print("Calculate")
    TestX = df
    # TestX = TestX.iloc[: , 1:] 
    TestX = TestX.iloc[: , 1:5]

    # Set for 1 container
    placeholder = st.empty() 

    # Add new
    IfNotUseDatabase = pd.DataFrame()

    # Name for dataset
    Name_for_database = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))

    ###### Sliding Windows
    First,Last = 0,390

    while Last <= len(TestX): 
        
        # count Time
        start_all= time.time()
   
        Position = TestX.iloc[First:Last]

        # If not use scale data
        scaled_newdf = Position

        Mean = pd.DataFrame()
        for x in scaled_newdf:
            total = scaled_newdf[x].mean()
            df2 = pd.DataFrame([total])
            Mean = pd.concat([Mean, df2], axis=1)

        Mean.columns = ['Mean1','Mean2','Mean3','Mean4']

        Median = pd.DataFrame()
        for x in scaled_newdf:
            total = scaled_newdf[x].median()
            df2 = pd.DataFrame([total])
            Median = pd.concat([Median, df2], axis=1)

        Median.columns = ['Median1','Median2','Median3','Median4']

        Std = pd.DataFrame()
        for x in scaled_newdf:
            total = scaled_newdf[x].std()
            df2 = pd.DataFrame([total])
            Std = pd.concat([Std, df2], axis=1)

        Std.columns = ['Std1','Std2','Std3','Std4']

        Mode = pd.DataFrame()
        for x in scaled_newdf:
            total = statistics.mode(scaled_newdf[x])
            df2 = pd.DataFrame([total])
            Mode = pd.concat([Mode, df2], axis=1)

        Mode.columns = ['Mode1','Mode2','Mode3','Mode4']

        Kurt = pd.DataFrame()
        for x in scaled_newdf:

            total = kurtosis(scaled_newdf[x],bias=False)
            df2 = pd.DataFrame([total])
            Kurt = pd.concat([Kurt, df2], axis=1)

        Kurt.columns = ['Kurtosis1','Kurtosis2','Kurtosis3',
                        'Kurtosis4']

        PtoP = pd.DataFrame()
        for x in scaled_newdf:

            total = scaled_newdf[x].max() + scaled_newdf[x].min()
            df2 = pd.DataFrame([total])
            PtoP = pd.concat([PtoP, df2], axis=1)

        PtoP.columns = ['PToP1','PToP2','PToP3','PToP4']

        # RMS = pd.DataFrame() 
        # for x in scaled_newdf:

        #     c = TestX[x]
        #     da1 = c.iloc[[0]]
        #     total = np.sqrt((da1**2).sum() / len(scaled_newdf[x]))
        #     df2 = pd.DataFrame([total])
        #     RMS = pd.concat([RMS, df2], axis=1)

        # RMS.columns = ['RMS1','RMS2','RMS3','RMS4']
        # # RMS.columns = ['RMS1','RMS2','RMS3','RMS4',
        # #                'RMS5','RMS6','RMS7','RMS8','RMS9']
        # # print(RMS)

        result = pd.concat([Mean, Median], axis=1)
        result = pd.concat([result, Std], axis=1)
        result = pd.concat([result, Mode], axis=1)
        result = pd.concat([result, Kurt], axis=1)
        result = pd.concat([result, PtoP], axis=1)
        # result = pd.concat([result, RMS], axis=1)

        
        newresult = result[['Std3','Std2','Mean2','Std1','PToP1','PToP4','PToP2','Std4','Kurtosis1','Kurtosis4']]
        # print(newresult)

        # Std3 = newresult.get("Std3")
        # Std2 = newresult.get("Std2")
        # Mean2 = newresult.get("Mean2")
        # Std1 = newresult.get("Std1")
        # PToP1 = newresult.get("PToP1")
        # PToP4 = newresult.get("PToP4")
        # PToP2 = newresult.get("PToP2")
        # Std4 = newresult.get("Std4")
        # Kurtosis1 = newresult.get("Kurtosis1")
        # Kurtosis4 = newresult.get("Kurtosis4")


        # To predict
        start_predict = time.time()
        OKNG,timeX,prediction_proba,prediction = predict(newresult) #Supervised And IsolationForest
        end_predict = time.time()
        # print("Time use predict: ",end_predict - start_predict)

        # print(OKNG,timeX,prediction_proba,prediction)

        # If_Not_use_database
        data = {
            "Result": [OKNG],
            "Time": [timeX],
            "Probability": [prediction_proba][0],
            "Prediction": [prediction][0],
            }
        result_for_predict = pd.DataFrame(data)
        result_for_predict = pd.concat([result_for_predict, newresult], axis=1)
        IfNotUseDatabase = pd.concat([IfNotUseDatabase,result_for_predict], axis=0)
        IfNotUseDatabase = IfNotUseDatabase.reset_index(drop=True)
        # print(IfNotUseDatabase)

        #if wanna see Result
        # print(okng,timeX,prediction_proba[0],prediction[0],Std3,Std2,Mean2,Std1,PToP1,PToP4,PToP2,Std4,Kurtosis1,Kurtosis4) 

        # ToFirebase
        # ToFirebase(OKNG,timeX,prediction_proba,prediction,Std3,Std2,Mean2,Std1,PToP1,PToP4,PToP2,Std4,Kurtosis1,Kurtosis4,Name_for_database)
        try:
            dataframeX = dataframe[["Result","Time","Probability","Prediction",'Std3','Std2','Mean2','Std1','PToP1','PToP4','PToP2','Std4','Kurtosis1','Kurtosis4']]
            IfNotUseDatabase = pd.concat([IfNotUseDatabase,dataframeX], axis=0)
        except:
            pass

        start = time.time()
        with placeholder.container():
            DataQ = Run(IfNotUseDatabase,Name_for_database)
            # Run()
        end = time.time()
        # print("Time use in Chart: ",end - start)


        First = First + Row 
        Last = Last + Row 

        # First = First + 5 # or + 10
        # Last = Last + 5 # or + 10

        end_all = time.time()
        # print("Time use all: ",end_all - start_all)
    # print(DataQ)
    # placeholder.empty()
    dataframe = pd.concat([dataframe,IfNotUseDatabase], axis=0)
    # print(dataframe)
    return dataframe




def BeforeMainProcess():
    # df = pd.DataFrame()
    # datax = {
    #         "Result": [1.0]
    #         }
    # df = pd.DataFrame(datax)
    df = pd.DataFrame()
    if df in st.session_state:
        st.session_state.df = df
    # else:
    #     st.session_state.df = df
    # st.sidebar.write(st.session_state.df)
    # st.session_state.df += 1
    # st.sidebar.write(st.session_state.df)
    st.sidebar.write(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10)))


    with st.sidebar:
        add_selectbox = st.selectbox(
                "Change Dataset",("Data1","Data2","Data3","Data4","Data5","Data6")
            )
        
        if "Data1" in add_selectbox: 
            data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv') # Ex = data.reset_index(drop=True)
        elif "Data2" in add_selectbox:
            data = pd.read_csv('Component/Data/Dataset/TotalFile36_37.csv') # Ex = data.reset_index(drop=True)
        elif "Data3" in add_selectbox:
            data = pd.read_csv('Component/Data/Dataset/TotalFile46_47.csv')
        elif "Data4" in add_selectbox:
            data = pd.read_csv('Component/Data/Dataset/TotalFile65_80.csv')
        elif "Data5" in add_selectbox:
            data = pd.read_csv('Component/Data/Dataset/TotalFile98_9c.csv')
        elif "Data6" in add_selectbox:
            data = pd.read_csv('Component/Data/Dataset/All134.csv')

    placeholder = st.empty()
    with placeholder.container():
        tab1, tab3 = st.tabs(["🎉 Welcome", "⚙️ Setting"])
        with tab1:
            st.markdown("# :black[คำอธิบายโปรเจค] ")
            col1, col2, col3 = st.columns([1.5,1,1])
            with col1:
                image = Image.open('Component/Picture/R04CPU.png')
                st.image(image, caption='R04CPU')
            with col2:
                st.write("")
                st.write("")
                st.write("""สำหรับหน้าเว็บนี้จะเป็น  Dashboard ไว้ใช้สำหรับดูและตรวจสอบผลการทำงานของ PLC  
                R04CPU (รูปด้านซ้ายมือ) โดยจะมีการแสดงผลทั้งแบบ กราฟเส้น กราฟวงกลม และตารางผลการทำงาน 
                ในขณะที่เครื่องทำงานอยู่""")

        with tab3:
            st.markdown("# :black[Change Row After Sliding Windows] ")
            Row_change = 5
            col1, col2 = st.columns((2,3))
            with col1:
                # Delete = st.button("Delete", key = "Database",use_container_width=False)
                Row = st.slider('Change Row After Sliding Windows', 1, 10, 10,label_visibility="visible")
                # Row = st.selectbox('How would you like to be contacted?',(5, 6, 7, 8, 9, 10))
            with col2:
                st.write("")
                if Row != Row_change:
                    st.success('Change Success!', icon="✅")
                else:
                    st.warning('Default Value of Row After Sliding Windows', icon="⚠️")

      
    Start = st.sidebar.button("Click here to start")
    if Start:
        # print("Start")
        placeholder.empty()
        st.session_state.key = MainProcess(data,Row,df)
    # st.write(st.session_state.key)
    try:
        st.session_state.df = pd.concat([st.session_state.df,st.session_state.key], axis=0)
        # st.session_state.df = st.session_state.key
        st.session_state.df = st.session_state.df.reset_index(drop=True)
        st.write(st.session_state.df)
        df = st.session_state.df
        # st.write(df)
    except:
        pass
    # st.write(st.session_state.df)

    
    # st.sidebar.title('Counter Example')
    # if 'count' not in st.session_state:
    #     st.session_state.count = 0

    # increment = st.sidebar.button('Increment')
    # if increment:
    #     st.session_state.count += 1

    #     st.sidebar.write('Count = ', st.session_state.count)


    
# For Test
# st.set_page_config(layout="wide")
# Start = st.button("Click here to start")
# if Start:
#     WTF()

# WTF()