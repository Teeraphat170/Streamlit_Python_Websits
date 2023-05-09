from datetime import datetime
from scipy.stats import kurtosis
from MainFile import MainProcess,BeforeMainProcess
from Login import Login
from threading import Thread
from firebase import firebase
from firebase_admin import credentials
from firebase_admin import db
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

st.set_page_config(page_icon=":bar_chart:", layout="wide")

# Start = st.button("Click here to start")
# if Start:
#     Login()

Login()

hide_st_style = """
            <style>

            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)












