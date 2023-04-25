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

data = pd.read_csv('Component/Data/Dataset/All134.csv')
data1 = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')
st.set_page_config(layout="wide",
                page_title="Hello",
                page_icon="👋",)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
# st.markdown("<h1 style='text-align: center; color: white;'>My Dashboard</h1>", unsafe_allow_html=True)

# col2, col3, col4 = st.columns((30,30,30))
# with col2:
#     key = st.selectbox("Key",['Name','Email','Age','Gender','Country','Sign Up Date', 'Profession','Salary'])
# with col3:
#     st.error('This is an error', icon="🚨")
#     st.warning('This is a warning', icon="⚠️")
#     progress_text = "Please wait."
#     my_bar = st.progress(0, text=progress_text)

#     for percent_complete in range(100):
#         # time.sleep(0.1)
#         my_bar.progress(percent_complete + 1, text=progress_text)
# with col4:
#     video_url = ("https://www.youtube.com/watch?v=BBDoNzIKXwQ&t=1s")
#     st.video(video_url )

# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )
