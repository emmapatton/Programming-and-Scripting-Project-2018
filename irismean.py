# Emma Patton, 2018-04-06
# Stats of iris data set using pandas
# Data obtained from: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

#Import the pandas library as pd
import pandas as pd
import numpy as np
from pprint import pprint 

#Load in the data with'read_csv()'

irisstats = pd.read_csv("data/iris.csv", header = None, names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"])

x = irisstats.describe()

print(irisstats.sample(5))
# pprint(x)





