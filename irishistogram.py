# Emma Patton, 2018-04-15 
# Histogram of Data 

# Reading from: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html
# https://pandas.pydata.org/pandas-docs/stable/visualization.html


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns

# import matplotlib.cm as cm
# import matplotlib.colors as colors
# from pprint import pprint 


irisstats = pd.read_csv("data/iris.csv", header = None, names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"])


# table = irisstats.describe()

x = irisstats.hist()

x[0][0].set_xlabel('length (cm)')
x[0][0].set_ylabel('count')

x[0][1].set_xlabel('width (cm)')
x[0][1].set_ylabel('count')

x[1][0].set_xlabel('length (cm)')
x[1][0].set_ylabel('count')

x[1][1].set_xlabel('width (cm)')
x[1][1].set_ylabel('count')


plt.show()

# https://machinelearningmastery.com/visualize-machine-learning-data-python-pandas/