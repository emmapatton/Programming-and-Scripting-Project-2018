# Emma Patton, 2018-04-06
# Stats of iris data set using pandas
# Data obtained from: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

#Import the pandas library as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint 

#Load in the data with'read_csv()'

irisstats = pd.read_csv("data/iris.csv", header = None, names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"])

# describe_result = irisstats.describe()

# twodp = describe_result.round(2)

# print(twodp)

# print(irisstats.sample(5))

# mean_result = irisstats.mean()

# meandp = mean_result.round(2)

# print(meandp)

# median_result = irisstats.median()

# print(median_result)

# standev_result = irisstats.std()

# standp = standev_result.round(2)

# print(standp)

# max_result = irisstats.max(numeric_only=1)

# print(max_result)

# min_result = irisstats.min(numeric_only=1)

# print(min_result)

# spearman_result = irisstats.corr(method='spearman')

# print(spearman_result) #https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient

# correl_result = irisstats.corr(method='pearson')

# print(correl_result)

#https://en.wikipedia.org/wiki/Correlation_coefficient



# boxplot = irisstats.boxplot(column = "Sepal Length")

# irisstats.plot(boxplot)


# plt.scatter(irisstats['Sepal Length'], irisstats['Sepal Width'])


irisstats.plot.scatter('Sepal Length', 'Sepal Width')


plt.show() # Depending on whether you use IPython or interactive mode, etc.

