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
import warnings
warnings.filterwarnings("ignore")

# data = pd.read_csv('Component/Data/Dataset/All134.csv')
# data1 = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')
# st.set_page_config(layout="wide",
#                 page_title="Hello",
#                 page_icon="👋",)

# st.write("# Welcome to Streamlit! 👋")

# st.sidebar.success("Select a demo above.")

# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )
# st.markdown("<h1 style='text-align: center; color: white;'>My Dashboard</h1>", unsafe_allow_html=True)
firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
firebaseDB.delete('/FinalProject','')

# test = st.button('Say hello')
# if test:
#     st.write('Why hello there')

col1, col2 = st.columns(2)

# Define CSS styles for the columns
col1_style = """
    border: 1px solid black;
    background-color: lightblue;
    padding: 10px;
"""

col2_style = """
    border: 1px solid black;
    background-color: lightgreen;
    padding: 10px;
"""

# Use the st.markdown function to apply the styles to the columns
with col1:
    st.markdown(f"<div style='{col1_style}'>Column 1</div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div style='{col2_style}'>Column 2</div>", unsafe_allow_html=True)