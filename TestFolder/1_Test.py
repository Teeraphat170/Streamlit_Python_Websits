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
import streamlit_authenticator as stauth
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
# firebaseDB = firebase.FirebaseApplication("https://finalproject-b05e3-default-rtdb.firebaseio.com/",None)
# firebaseDB.delete('/FinalProject','')

# test = st.button('Say hello')
# if test:
#     st.write('Why hello there')

# col1, col2 = st.columns(2)

# # Define CSS styles for the columns
# col1_style = """
#     border: 1px solid black;
#     background-color: lightblue;
#     padding: 10px;
# """

# col2_style = """
#     border: 1px solid black;
#     background-color: lightgreen;
#     padding: 10px;
# """

# # Use the st.markdown function to apply the styles to the columns
# with col1:
#     st.markdown(f"<div style='{col1_style}'>Column 1</div>", unsafe_allow_html=True)

# with col2:
#     st.markdown(f"<div style='{col2_style}'>Column 2</div>", unsafe_allow_html=True)

data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')
data1 = pd.read_csv('Component/Data/Dataset/All134.csv')
# Ex = data.reset_index(drop=True)
# Ex1 = data1.reset_index(drop=True)

# new = Ex[["level_2","level_3","level_4","level_5","[LOGGING]","RD81DL96_1","2","3","4"]]
# print(new)

# data = data.iloc[: , 1:5] 
    
# # count Time
# start = time.time()

# # Add new

# ##### Sliding Windows
# First,Last = 0,390

# while Last <= len(data): 
   
#     Position = data.iloc[First:Last]
    
#     # If not use scale data
#     scaled_newdf = Position

#     Mean = pd.DataFrame()
#     for x in scaled_newdf:
#         total = scaled_newdf[x].mean()
#         df2 = pd.DataFrame([total])
#         Mean = pd.concat([Mean, df2], axis=1)
#     # print(Mean)
#     Mean.columns = ['Mean1','Mean2','Mean3','Mean4']
#     First = First + 5
#     Last = Last + 5


# print(Mean)
# end = time.time()
# print("Time use : ",end - start)
# import yaml
# from yaml.loader import SafeLoader
# import streamlit_authenticator as stauth 

# with open('../config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# import string
# import random

# xx = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
# print ("grgrg:{}".format(xx))
# import streamlit as st

# st.title('Counter Example')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# increment = st.button('Increment')
# if increment:
#     st.session_state.count += 1

# st.write('Count = ', st.session_state.count)

hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
print(hashed_passwords)