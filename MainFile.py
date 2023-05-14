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

def FromDatabase():
    df = pd.DataFrame()
    firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
    result = firebaseDB.get('/FinalProject', '')

    Prediction = pd.DataFrame()
    Probability = pd.DataFrame()
    Result = pd.DataFrame()
    Time = pd.DataFrame()
    Std3 = pd.DataFrame()
    Std2 = pd.DataFrame()
    Mean2 = pd.DataFrame()
    Std1 = pd.DataFrame()
    PToP1 = pd.DataFrame()
    PToP4 = pd.DataFrame()
    PToP2 = pd.DataFrame()
    Std4 = pd.DataFrame()
    Kurtosis1 = pd.DataFrame()
    Kurtosis4 = pd.DataFrame()
    Total = pd.DataFrame()

    for key, value in result.items():

        Prediction_in_loop = pd.DataFrame(value["Prediction"],columns=["Prediction"])
        Probability_in_loop = pd.DataFrame(value["Probability"],columns=["Probability"])
        Result_in_loop = pd.DataFrame(value["Result"],columns=["Result"])
        Time_in_loop = pd.DataFrame(value["Time"],columns=["Time"])
        Std3_in_loop = pd.DataFrame(value["Std3"],columns=["Std3"])
        Std2_in_loop = pd.DataFrame(value["Std2"],columns=["Std2"])
        Mean2_in_loop = pd.DataFrame(value["Mean2"],columns=["Mean2"])
        Std1_in_loop = pd.DataFrame(value["Std1"],columns=["Std1"])
        PToP1_in_loop = pd.DataFrame(value["PToP1"],columns=["PToP1"])
        PToP4_in_loop = pd.DataFrame(value["PToP4"],columns=["PToP4"])
        PToP2_in_loop = pd.DataFrame(value["PToP2"],columns=["PToP2"])
        Std4_in_loop = pd.DataFrame(value["Std4"],columns=["Std4"])
        Kurtosis1_in_loop = pd.DataFrame(value["Kurtosis1"],columns=["Kurtosis1"])
        Kurtosis4_in_loop = pd.DataFrame(value["Kurtosis4"],columns=["Kurtosis4"])

        Prediction = pd.concat([Prediction, Prediction_in_loop], axis=0)
        Prediction = Prediction.reset_index(drop=True)
        Probability = pd.concat([Probability, Probability_in_loop], axis=0)
        Probability = Probability.reset_index(drop=True)
        Result = pd.concat([Result, Result_in_loop], axis=0)
        Result = Result.reset_index(drop=True)
        Time = pd.concat([Time, Time_in_loop], axis=0)
        Time = Time.reset_index(drop=True)
        Std3 = pd.concat([Std3, Std3_in_loop], axis=0)
        Std3 = Std3.reset_index(drop=True)
        Std2 = pd.concat([Std2, Std2_in_loop], axis=0)
        Std2 = Std2.reset_index(drop=True)
        Mean2 = pd.concat([Mean2, Mean2_in_loop], axis=0)
        Mean2 = Mean2.reset_index(drop=True)
        Std1 = pd.concat([Std1, Std1_in_loop], axis=0)
        Std1 = Std1.reset_index(drop=True)
        PToP1 = pd.concat([PToP1, PToP1_in_loop], axis=0)
        PToP1 = PToP1.reset_index(drop=True)
        PToP4 = pd.concat([PToP4, PToP4_in_loop], axis=0)
        PToP4 = PToP4.reset_index(drop=True)
        PToP2 = pd.concat([PToP2, PToP2_in_loop], axis=0)
        PToP2 = PToP2.reset_index(drop=True)
        Std4 = pd.concat([Std4, Std4_in_loop], axis=0)
        Std4 = Std4.reset_index(drop=True)
        Kurtosis1 = pd.concat([Kurtosis1, Kurtosis1_in_loop], axis=0)
        Kurtosis1 = Kurtosis1.reset_index(drop=True)
        Kurtosis4 = pd.concat([Kurtosis4, Kurtosis4_in_loop], axis=0)
        Kurtosis4 = Kurtosis4.reset_index(drop=True)

    Total = pd.concat([Total, Prediction], axis=1)
    Total = pd.concat([Total, Probability], axis=1)
    Total = pd.concat([Total, Result], axis=1)
    Total = pd.concat([Total, Time], axis=1)
    Total = pd.concat([Total, Std3], axis=1)
    Total = pd.concat([Total, Std2], axis=1)
    Total = pd.concat([Total, Mean2], axis=1)
    Total = pd.concat([Total, Std1], axis=1)
    Total = pd.concat([Total, PToP1], axis=1)
    Total = pd.concat([Total, PToP4], axis=1)
    Total = pd.concat([Total, PToP2], axis=1)
    Total = pd.concat([Total, Std4], axis=1)
    Total = pd.concat([Total, Kurtosis1], axis=1)
    Total = pd.concat([Total, Kurtosis4], axis=1)
    # print(Total)
    return Total


# Main
def MainProcess(df,Row,dataframe,Remain_Or_Not,options1,options2):
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

    Data_From_Database = pd.DataFrame()

    # Fromdatabase
    try:
        Data_From_Database = FromDatabase()
        # print(Data_From_Database)
    except:
        pass

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

        if Remain_Or_Not == 0:
            Data_From_Database = pd.DataFrame()

        start = time.time()
        with placeholder.container():
            DataQ = Run(IfNotUseDatabase,Data_From_Database,options1,options2)
            # Run()
        end = time.time()
        # print("Time use in Chart: ",end - start)


        First = First + Row 
        Last = Last + Row 

        # First = First + 5 # or + 10
        # Last = Last + 5 # or + 10

        end_all = time.time()
        # print("Time use all: ",end_all - start_all)

    # st.dataframe(IfNotUseDatabase)
    if Remain_Or_Not == "Collect":
        dataframe = pd.concat([dataframe,IfNotUseDatabase], axis=0)
        ToFirebase(dataframe)

    # print(dataframe)
    return dataframe




def BeforeMainProcess(dataframe):
    # st.sidebar.write(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10)))
    Row = 5
    Remain_Or_Not = 0
    with st.sidebar:
        add_selectbox = st.selectbox(
                "⚙️ Change Dataset",("Data1","Data2","Data3","Data4","Data5","Data6")
            )
        
        if "Data1" in add_selectbox: 
            data = pd.read_csv('Component/Data/Dataset/All134.csv') # Ex = data.reset_index(drop=True)
        elif "Data2" in add_selectbox:
            data = pd.read_csv('Component/Data/Dataset/TotalFile36_37.csv') # Ex = data.reset_index(drop=True)
        elif "Data3" in add_selectbox:
            data = pd.read_csv('Component/Data/Dataset/TotalFile46_47.csv')
        elif "Data4" in add_selectbox:
            data = pd.read_csv('Component/Data/Dataset/TotalFile65_80.csv')
        elif "Data5" in add_selectbox:
            data = pd.read_csv('Component/Data/Dataset/TotalFile98_9c.csv')
        elif "Data6" in add_selectbox:
            # data = pd.read_csv('Component/Data/Dataset/All134.csv')
            data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')
            
    placeholder = st.empty()
    with placeholder.container():
        # tab1, tab3 = st.tabs(["🎉 Welcome", "⚙️ Setting"])
        # with tab1:
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

        # with tab3:
            # st.header(":black[Change Row After Sliding Windows] ")
            # Row_change = 5
            # col1, col2 = st.columns((2,3))
            # with col1:
            #     Row = st.slider('Change Row After Sliding Windows', 1, 10, 10,label_visibility="visible")
            #     if Row not in st.session_state:
            #         st.session_state.Row = Row

            # with col2:
            #     st.write("")
            #     if Row != Row_change:
            #         st.success('Change Success!', icon="✅")
            #     else:
            #         st.warning('Default Value of Row After Sliding Windows', icon="⚠️")

            # st.header(":black[Data After Start Finish] ")
            # col3, col4 = st.columns((2,3))
            # with col3:
            #     Remain_Data = st.radio("Want To Remain Data After Start?",('Yes', 'No'),index=1)
            # with col4:
            #     st.write("")
            #     if Remain_Data == 'No':
            #         Remain_Or_Not = 0
            #         st.write("")
            #         st.warning('If select Yes Data after run will be Remain', icon="⚠️")  
            #     else:
            #         Remain_Or_Not = 1
            #         st.write("")
            #         st.success('Change Success!', icon="✅")

            # st.header(":black[Delete data from database] ")
            # col5, col6 = st.columns((2,3))
            # with col5:
            #     st.write("")
            #     Delete = st.button("Delete", key = "Database",use_container_width=True)

            # with col6:
                
            #     if Delete:
            #         firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
            #         firebaseDB.delete('/', '')
            #         st.success('Change Delete!', icon="✅")
            #     else:
            #         st.warning('It will all delete data from database', icon="⚠️")


    # option = st.sidebar.selectbox('Setting',('Not Change', 'Change'), index = 0 , key="visibility")

    
    # if "visibility" not in st.session_state:
    #     st.session_state.visibility = "Change"
    # if "Row" not in st.session_state:
    #     st.session_state["Row"] = 10

    # if "Remain_Data" not in st.session_state:
    #     st.session_state["Remain_Data"] = 0

    option = st.sidebar.selectbox('⚙️ Setting', options=['Not Change', 'Change'], index = 0 , key="visibility")
    if option == "Change":
        Row = st.sidebar.slider('Change Row After Sliding Windows', 1, 10, 5,label_visibility="visible")
        st.session_state["Row"] = Row
        # st.sidebar.write(Row)
        Remain_Data = st.sidebar.radio("Want To Remain Data After Start?",('Yes', 'No'),index=1, key="Database")
        if Remain_Data == 'No':
            Remain_Or_Not = "Not Collect"
            st.session_state["Remain_Data"] = Remain_Or_Not
        else:
            Remain_Or_Not = "Collect"
            st.session_state["Remain_Data"] = Remain_Or_Not
        st.sidebar.write("⚠️ Delete all remain data ⚠️")
        Delete = st.sidebar.button("Delete", key = "Delete_Database",use_container_width=True)
        if Delete:
            firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
            firebaseDB.delete('/', '')
        options1 = st.sidebar.multiselect('Select Features In Line chart 1',["Std3","Std2","Mean2","Std1","PToP1"],
                                         ["Std3","Std2","Mean2","Std1","PToP1"],key='LineChart1')
        if options1:
            st.session_state["Line_Chart1"] = options1

        options2 = st.sidebar.multiselect('Select Features In Line chart 2',["PToP4","PToP2","Std4","Kurtosis1","Kurtosis4"],
                                         ["PToP4","PToP2","Std4","Kurtosis1","Kurtosis4"],key='LineChart2')
        if options2:
            st.session_state["Line_Chart2"] = options2


    # st.sidebar.write(st.session_state)
    Start = st.sidebar.button("Click here to start",use_container_width=True)
    if Start:
        # print("Start")
        placeholder.empty()
        MainProcess(data,st.session_state["Row"],dataframe,st.session_state["Remain_Data"],st.session_state["Line_Chart1"],st.session_state["Line_Chart2"])


    
        # st.title('Counter Example')
        # if 'count' not in st.session_state:
        #     st.session_state.count = 0

        # increment = st.button('Increment')
        # if increment:
        #     st.session_state.count += 1

        #     st.sidebar.write('Count = ', st.session_state.count)


    
# For Test
# st.set_page_config(layout="wide")
# Start = st.button("Click here to start")
# if Start:
#     WTF()

# WTF()