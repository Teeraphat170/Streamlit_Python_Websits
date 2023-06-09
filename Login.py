import pickle
from pathlib import Path
from MainFile import BeforeMainProcess
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth  # pip install streamlit-authenticator


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
# st.set_page_config(page_icon=":bar_chart:", layout="wide")

def Login():
    # --- USER AUTHENTICATION ---
    names = ["Teeraphat","Admin","Admin1"]
    usernames = ["Teeraphat","Admin","Admin1"]

    # load hashed passwords
    file_path = Path(__file__).parent / "Component/Hashed_Password/hashed_pw.pkl"
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

    authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
        "sales_dashboard", "abcdef", cookie_expiry_days=10)

    name, authentication_status, username = authenticator.login("Login", "main")

    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")

    if authentication_status:
        # st.session_state.key = name,username
        st.sidebar.title(f'Welcome *{st.session_state["name"]}*')
        authenticator.logout("Logout", "sidebar")

        dataframe = pd.DataFrame()

        # if "Row" not in st.session_state:
        #     st.session_state["Row"] = 10

        # if "Remain_Data" not in st.session_state:
        #     st.session_state["Remain_Data"] = 0
        
        BeforeMainProcess(dataframe)
 

#         # Start = st.sidebar.button("Click here to start")
#         # if Start:
#         #     WTF(data) 

