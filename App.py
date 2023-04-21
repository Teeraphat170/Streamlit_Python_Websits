from datetime import datetime
from scipy.stats import kurtosis
from MainFile import ReadCSV
from threading import Thread
# import ray
import time
import pickle
import streamlit as st
import statistics
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")


def Test():
    data = pd.read_csv('Data/Dataset/TotalFile35_36.csv')
    ForTest = data
    ForTest = ForTest["level_2"].head(50)
    DataQ = pd.DataFrame(ForTest)

    placeholder = st.empty()

    for seconds in range(10):

        list = []
        i = 0
        while i < len(ForTest.index):
            i = i + 1
            list.append(i)
            X = pd.DataFrame(list,columns = ['X-axis'])

            result = pd.concat([X, DataQ], axis=1)

        with placeholder.container():

            st.line_chart(result, x='X-axis')
            time.sleep(1)

if __name__ == '__main__':
    Test()

# def fun1():
#     time = datetime.today().strftime('%H:%M:%S')
#     print("Working1",time)
# def fun2():
#     time1 = datetime.today().strftime('%H:%M:%S')
#     print("Working2",time1)

# t1 = Thread(target=fun1)
# t2 = Thread(target=fun2)

# t1.start()
# t2.start()





# st.write(data)

# Result,timeX,prediction_proba,prediction = ReadCSV(data)
# print(Result,timeX,prediction_proba,prediction)

