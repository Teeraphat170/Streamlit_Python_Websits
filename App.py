import streamlit as st
from Data.MainFile import ReadCSV
import numpy as np
import pandas as pd
import pickle

TestX = pd.read_csv('Data/Dataset/All134.csv')
# print(TestX)

# load_clf = pickle.load(open('Data/Model/IsolationForest_7.pkl', 'rb'))
# print(load_clf)

Result,timeX,prediction_proba,prediction = ReadCSV(TestX)
print(Result,timeX,prediction_proba,prediction)