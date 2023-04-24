from datetime import datetime
from scipy.stats import kurtosis
from Component.MainFile import ReadCSV
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
data = pd.read_csv('Data/Dataset/TotalFile35_36.csv')

















