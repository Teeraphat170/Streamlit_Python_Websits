# from MainFile import ReadCSV
from datetime import datetime
from scipy.stats import kurtosis
from MainFile import ReadCSV
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


data = pd.read_csv('Data/Dataset/TotalFile35_36.csv')
ForTest = data
ForTest = ForTest["level_2"].head(10)
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









# st.write(data)

# Result,timeX,prediction_proba,prediction = ReadCSV(data)
# print(Result,timeX,prediction_proba,prediction)

