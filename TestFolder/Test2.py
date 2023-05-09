from firebase import firebase
import pandas as pd
import time
import numpy as np
import streamlit as st
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import numpy as np
import pandas as pd
# from Predict import predict
import statistics
import pickle
import time
from datetime import datetime
from scipy.stats import kurtosis
from firebase import firebase
from firebase_admin import db
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")


# data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')
# data1 = pd.read_csv('Component/Data/Dataset/All134.csv')
# Ex = data.reset_index(drop=True)
# Ex1 = data1.reset_index(drop=True)

# new = Ex[["level_2","level_3","level_4","level_5","[LOGGING]","RD81DL96_1","2","3","4"]]


# data = {
#   "calories": [420, 380, 390, 380, 400, 390],
#   "duration": [50, 40, 45, 50, 50, 45],
#   "test":[12, 16, 15, 16, 15, 19],
#     "calories1": [420, 380, 390, 380, 400, 390],
#   "duration1": [50, 40, 45, 50, 50, 45],
#   "test1":[12, 16, 15, 16, 15, 19],
#     "calories3": [420, 380, 390, 380, 400, 390],
#   "duration3": [50, 40, 45, 50, 50, 45],
#   "test3":[12, 16, 15, 16, 15, 19],
#     "calories4": [420, 380, 390, 380, 400, 390],
#   "duration4": [50, 40, 45, 50, 50, 45],
#   "test4":[12, 16, 15, 16, 15, 19],
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)
# # TimeX = df["Time"]
# # print(DataQ)
# # # print(df)
# # st.line_chart(DataQ ,x=DataQ.index)
# st.set_page_config(layout="wide")



# with open('TestFolder/Test.css') as f: # Test.css with command prompt : TestFolder/Test.css with PowerShell
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# def Test(Ex):
#       col1, col2 = st.columns((30,30))
#       with col1:
#           st.header("Line Chart")
#           st.line_chart(df["calories"])
#           # st.line_chart(Ex1["RD81DL96_1"])
#       with col2:
#           st.header("Dataframe")
#           # st.dataframe(df)
#           st.dataframe(Ex)

#       col3, col4 = st.columns(2)
#       with col3:  
#           fig = px.line(df, x = 'test',y = df.columns[:-1])
#           st.plotly_chart(fig,use_container_width=True, sharing="streamlit", theme="streamlit")  
#       with col4:
#           Prediction1 = len(df[df['calories']==400])
#           Prediction_1 = len(df[df['duration']==50])
#           piechart = [Prediction1,Prediction_1]
#           detection = ['Normally','Anomaly']
#           fig = px.pie(values=piechart,names=detection)

#           st.header("Pie Chart")
#           st.plotly_chart(fig, use_container_width=True)

# tab1, tab2 ,tab3= st.tabs(["🎉 Welcome", "📈 Dashboard","⚙️ Setting"])
# with tab1:
#   st.markdown("# :green[Welcome] ")

# with tab3:
#   add_selectbox = st.selectbox(
#     "Change Dataset",
#     ("data1","data2" )
#   )

#   if "data1" in add_selectbox: # If user selects Email  do 👇
#     data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')
#     Ex = data.reset_index(drop=True)
#   else:
#     data1 = pd.read_csv('Component/Data/Dataset/All134.csv')
#     Ex = data1.reset_index(drop=True)

# with tab2:
#   st.markdown("# :green[Anomaly Detection Dashborad] 📈")
#   st.markdown("#")
#   Test(Ex)

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )
# col2.markdown(
#     """
#     <style>
#     .st-b8 {
#         border: 2px solid black;
#         padding: 10px;
#         border-radius: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# col1.markdown(
#     """
#     <style>
#     .st-b9 {
#         border: 2px solid black;
#         padding: 10px;
#         border-radius: 10px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# data = pd.read_csv('Data/Dataset/All134.csv')
data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')

def MainProcess(df):
    # print("Calculate")
    TestX = df
    # TestX = TestX.iloc[: , 1:] 
    TestX = TestX.iloc[: , 1:5]
    
    # count Time
    start = time.time()

    # Set for 1 container

    # Add new
    # df = pd.DataFrame()


    ###### Sliding Windows
    First,Last = 0,390

    while Last <= 610: 
        start = time.time()
        Position = TestX.iloc[First:Last]

        # If not use scale data
        scaled_newdf = Position
        # print(scaled_newdf)

        df = pd.DataFrame()

        # Mean = pd.DataFrame()
        # start = time.time()
        # for x in scaled_newdf:
        #     # print(x)
        #     total = scaled_newdf[x].mean()
        #     df2 = pd.DataFrame([total])
        #     Mean = pd.concat([Mean, df2], axis=1)
        
        # end = time.time()
        # Mean.columns = ['Mean1','Mean2','Mean3','Mean4']
        # print(Mean)
        # print("Time use : ",end - start)
        # fef = ["level_2","level_3","level_4","level_5"]
        # print(scaled_newdf["level_2"],scaled_newdf["level_3"],scaled_newdf["level_4"],scaled_newdf["level_5"])
        
        # Mean
        total1 = scaled_newdf["level_2"].mean()
        total2 = scaled_newdf["level_3"].mean()
        total3 = scaled_newdf["level_4"].mean()
        total4 = scaled_newdf["level_5"].mean()

        Mean = {
            'Mean1':[total1],
            'Mean2':[total2],
            'Mean3':[total3],
            'Mean4':[total4],
        }
        Mean = pd.DataFrame(Mean)

        # print(Mean)
        # print("Time use : ",end - start)

        # Median = pd.DataFrame()
        # for x in scaled_newdf:
        #     total = scaled_newdf[x].median()
        #     df2 = pd.DataFrame([total])
        #     Median = pd.concat([Median, df2], axis=1)

        # Median.columns = ['Median1','Median2','Median3','Median4']

        # Median
        total1 = scaled_newdf["level_2"].median()
        total2 = scaled_newdf["level_3"].median()
        total3 = scaled_newdf["level_4"].median()
        total4 = scaled_newdf["level_5"].median()

        Median = {
            'Median1':[total1],
            'Median2':[total2],
            'Median3':[total3],
            'Median4':[total4],
        }
        Median = pd.DataFrame(Median)



        # Std = pd.DataFrame()
        # for x in scaled_newdf:
        # # for x in TestX:
        #     total = scaled_newdf[x].std()
        #     df2 = pd.DataFrame([total])
        #     Std = pd.concat([Std, df2], axis=1)

        # Std.columns = ['Std1','Std2','Std3','Std4']

        # Std
        total1 = scaled_newdf["level_2"].std()
        total2 = scaled_newdf["level_3"].std()
        total3 = scaled_newdf["level_4"].std()
        total4 = scaled_newdf["level_5"].std()

        Std = {
            'Std1':[total1],
            'Std2':[total2],
            'Std3':[total3],
            'Std4':[total4],
        }
        Std = pd.DataFrame(Std)



        # Mode = pd.DataFrame()
        # for x in scaled_newdf:
        #     total = statistics.mode(scaled_newdf[x])
        #     df2 = pd.DataFrame([total])
        #     Mode = pd.concat([Mode, df2], axis=1)

        # Mode.columns = ['Mode1','Mode2','Mode3','Mode4']

        # Mode
        total1 = statistics.mode(scaled_newdf["level_2"])
        total1 = statistics.mode(scaled_newdf["level_3"])
        total1 = statistics.mode(scaled_newdf["level_4"])
        total1 = statistics.mode(scaled_newdf["level_5"])

        Mode = {
            'Mode1':[total1],
            'Mode2':[total2],
            'Mode3':[total3],
            'Mode4':[total4],
        }
        Mode = pd.DataFrame(Mode)

        # Kurt = pd.DataFrame()
        # for x in scaled_newdf:

        #     total = kurtosis(scaled_newdf[x],bias=False)
        #     df2 = pd.DataFrame([total])
        #     Kurt = pd.concat([Kurt, df2], axis=1)

        # Kurt.columns = ['Kurtosis1','Kurtosis2','Kurtosis3',
        #                 'Kurtosis4']

        # Kurtosis
        total1 = kurtosis(scaled_newdf["level_2"],bias=False)
        total1 = kurtosis(scaled_newdf["level_3"],bias=False)
        total1 = kurtosis(scaled_newdf["level_4"],bias=False)
        total1 = kurtosis(scaled_newdf["level_5"],bias=False)

        Kurt = {
            'Kurtosis1':[total1],
            'Kurtosis2':[total2],
            'Kurtosis3':[total3],
            'Kurtosis4':[total4],
        }
        Kurt = pd.DataFrame(Kurt)


        # PtoP = pd.DataFrame()
        # for x in scaled_newdf:

        #     total = scaled_newdf[x].max() + scaled_newdf[x].min()
        #     df2 = pd.DataFrame([total])
        #     PtoP = pd.concat([PtoP, df2], axis=1)

        # PtoP.columns = ['PToP1','PToP2','PToP3','PToP4']

        # PtoP
        total1 = scaled_newdf["level_2"].max() + scaled_newdf["level_2"].min()
        total1 = scaled_newdf["level_3"].max() + scaled_newdf["level_3"].min()
        total1 = scaled_newdf["level_4"].max() + scaled_newdf["level_4"].min()
        total1 = scaled_newdf["level_5"].max() + scaled_newdf["level_5"].min()

        PtoP = {
            'PToP1':[total1],
            'PToP2':[total2],
            'PToP3':[total3],
            'PToP4':[total4],
        }
        PtoP = pd.DataFrame(PtoP)


        # RMS = pd.DataFrame() 
        # for x in scaled_newdf:

        #     # c = TestX[x]
        #     # da1 = c.iloc[[0]]
        #     # print(da1)
        #     total = np.sqrt((scaled_newdf[x]**2).sum() / len(scaled_newdf[x]))
        #     print("yes :",scaled_newdf[x]**2)
        #     print("not : ",scaled_newdf[x])
        #     df2 = pd.DataFrame([total])
        #     RMS = pd.concat([RMS, df2], axis=1)

        # RMS.columns = ['RMS1','RMS2','RMS3','RMS4']

        total1 = np.sqrt((scaled_newdf["level_2"]**2).sum() / len(scaled_newdf["level_2"]))
        total1 = np.sqrt((scaled_newdf["level_3"]**2).sum() / len(scaled_newdf["level_3"]))
        total1 = np.sqrt((scaled_newdf["level_4"]**2).sum() / len(scaled_newdf["level_4"]))
        total1 = np.sqrt((scaled_newdf["level_5"]**2).sum() / len(scaled_newdf["level_5"]))

        RMS = {
            'RMS1':[total1],
            'RMS2':[total2],
            'RMS3':[total3],
            'RMS4':[total4],
        }
        RMS = pd.DataFrame(RMS)

        result = pd.concat([Mean, Median], axis=1)
        result = pd.concat([result, Std], axis=1)
        result = pd.concat([result, Mode], axis=1)
        result = pd.concat([result, Kurt], axis=1)
        result = pd.concat([result, PtoP], axis=1)
        result = pd.concat([result, RMS], axis=1)

        
        newresult = result[['Std3','Std2','Mean2','Std1','PToP1','PToP4','PToP2','Std4','Kurtosis1','Kurtosis4']]
        dot_time = datetime.today().strftime('%H:%M:%S')
        df = newresult

        load_clf = pickle.load(open('Component/Data/Model/IsolationForest_7.pkl', 'rb')) 

        # IsolationForest
        prediction = load_clf.predict(df) 
        prediction_proba = load_clf.decision_function(df)

        
        if prediction[0] == -1 and prediction_proba[0] < 0:
            OKNG = 'NG'
            # OKNG = 'OK'
        else:
            OKNG = 'OK'
        end = time.time()
        # print("Time use : ",end - start)

        First = First + 5 # or + 5
        Last = Last + 5 # or + 5
        print(OKNG,dot_time,prediction_proba,prediction)

MainProcess(data)