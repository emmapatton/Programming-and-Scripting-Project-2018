# Emma Patton, 2018-04-15 
# Histogram of Data 

# Reading from: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html
# https://pandas.pydata.org/pandas-docs/stable/visualization.html


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import matplotlib.cm as cm
# import matplotlib.colors as colors
# from pprint import pprint 


irisstats = pd.read_csv("data/iris.csv", header = None, names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"])

irisstats.hist()