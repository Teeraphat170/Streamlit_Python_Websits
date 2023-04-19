# from MainFile import ReadCSV
from datetime import datetime
from scipy.stats import kurtosis
from MainFile import ReadCSV
import pickle
import streamlit as st
import statistics
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

TestX = pd.read_csv('Data/Dataset/All134.csv')
# print(TestX)




st.write(TestX)

# Result,timeX,prediction_proba,prediction = ReadCSV(TestX)
# print(Result,timeX,prediction_proba,prediction)

