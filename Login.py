import pickle
from pathlib import Path
from MainFile import WTF
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
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
        with st.sidebar:
            st.sidebar.title(f"Welcome {name}")
            authenticator.logout("Logout", "sidebar")
            add_selectbox = st.selectbox(
                    "Change Dataset",("data1","data2" )
                    )
                
            if "data1" in add_selectbox: # If user selects Email  do 👇
                data = pd.read_csv('Component/Data/Dataset/TotalFile35_36.csv')
                Ex = data.reset_index(drop=True)
            else:
                data = pd.read_csv('Component/Data/Dataset/All134.csv')
                Ex = data.reset_index(drop=True)

        Start = st.sidebar.button("Click here to start")
        if Start:
            WTF(data) 

        tab1, tab2, tab3 = st.tabs(["🎉 Welcome", "📈 Dashboard", "⚙️ Setting"])
        with tab1:
            st.markdown("# :green[Welcome] ")
        with tab3:
            st.markdown("# :green[Anomaly Detection Dashborad] ")
            st.markdown("#")
        with tab2:
            st.markdown("# :green[Anomaly Detection Dashborad] ")
            st.markdown("#")

        # Stop = st.sidebar.button("Click here to Stop")
        # if Stop:
        #     st.stop() 
        
        