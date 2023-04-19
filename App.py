import streamlit as st
from Data.MainFile import ReadCSV
import numpy as np
import pandas as pd

TestX = pd.read_csv('Data/Dataset/All134.csv')
# print(TestX)
Result,timeX,prediction_proba,prediction = ReadCSV(TestX)

print(Result,timeX,prediction_proba,prediction)