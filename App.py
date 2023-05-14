from Login import Login
# import ray
import firebase_admin
import threading
import multiprocessing
import multiprocessing.pool
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
# import warnings
# warnings.filterwarnings("ignore")
# data = pd.read_csv('Data/Dataset/TotalFile35_36.csv')

st.set_page_config(page_title="Anomaly Detection for Predictive Maintenance",page_icon=":bar_chart:", layout="wide")

# Start = st.button("Click here to start")
# if Start:
#     Login()

Login()

hide_st_style = """
                <style>
                # MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                
                </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



# header {visibility: hidden;}








