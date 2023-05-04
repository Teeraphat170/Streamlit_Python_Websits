
import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Teeraphat","Admin","Admin1"]
usernames = ["Teeraphat","Admin","Admin1"]
passwords = ["12345","Admin","Admin1"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)