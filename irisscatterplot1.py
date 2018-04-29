# Emma Patton, 2018-04-15 
# Scatter Plot of Data

# Reading from: http://pandas.pydata.org/pandas-docs/version/0.15.0/visualization.html


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import matplotlib.cm as cm
# import matplotlib.colors as colors
# from pprint import pprint 


irisstats = pd.read_csv("data/iris.csv", header = None, names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"])


# boxplot = irisstats.boxplot(column = "Sepal Length")

# irisstats.plot(boxplot)


# plt.scatter(irisstats['Sepal Length'], irisstats['Sepal Width'])


irisstats.plot.scatter('Sepal Length', 'Sepal Width')
irisstats.plot.scatter('Petal Length', 'Petal Width')


# ?Figure out how to plot this using colours and a key - ?Seaborn?? 
# Also look into box plots

plt.show() 


