# from MainFile import ReadCSV
from datetime import datetime
from scipy.stats import kurtosis
from MainFile import ReadCSV
import pickle
import streamlit as st
import statistics
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TestX = pd.read_csv('Data/Dataset/All134.csv')
print(TestX)

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)
st.title("Real-Time / Live Data Science Dashboard")
job_filter = st.selectbox("Select the Job", pd.unique(TestX["Unnamed: 0"]))


# st.write("Hello Streamlit!")

# Result,timeX,prediction_proba,prediction = ReadCSV(TestX)
# print(Result,timeX,prediction_proba,prediction)

