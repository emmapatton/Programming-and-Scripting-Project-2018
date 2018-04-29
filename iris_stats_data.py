# Emma Patton, 2018-04-06
# Stats of iris data set using pandas
# Data obtained from: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

#Import the pandas library as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint 

heading = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

#Load in the data with'read_csv()'
irisstats = pd.read_csv("data/iris.csv", header = None, names = [*heading, "Species"]) #I needed to add "Species" on to the end of my header so I used the spread operator (*)



irisstats_group_bys = irisstats.groupby(['Species'])


setosa_df = irisstats_group_bys.get_group('Iris-setosa')
setosa_df.name = 'Iris-setosa'

versicolor_df = irisstats_group_bys.get_group('Iris-versicolor')
versicolor_df.name = 'Iris-versicolor'

virginica_df = irisstats_group_bys.get_group('Iris-virginica')
virginica_df.name = 'Iris-virginica'


def getIrisStats(species):
    count = species.count()
    mean = species.mean()
    median = species.median()
    stan_dev = species.std()
    min = species.min(numeric_only=1)
    max = species.max(numeric_only=1)

    species_columnwidth = '             {:^12}  {:^12}  {:^12}  {:^12}'
    num_columnwidth = '{:12} {:^12.2f}  {:^12.2f}  {:^12.2f}  {:^12.2f}'

    print(species.name)
    print(species_columnwidth.format(*heading))
    print(num_columnwidth.format('Count', *count.values))
    print(num_columnwidth.format('Mean', *mean.values))
    print(num_columnwidth.format('Median', *median.values))
    print(num_columnwidth.format('Stand Dev', *stan_dev.values))
    print(num_columnwidth.format('Min', *min.values))
    print(num_columnwidth.format('Max', *max.values))
    print('')


getIrisStats(setosa_df)
getIrisStats(versicolor_df)
getIrisStats(virginica_df)

def showScatterIris(setosa, versicolor, virginica, column_1, column_2):

    x1 = setosa[column_1]
    y1 = setosa[column_2]
    x2 = versicolor[column_1]
    y2 = versicolor[column_2]
    x3 = virginica[column_1]
    y3 = virginica[column_2]

    plt.title(column_1 + " vs. " + column_2)
    plt.xlabel(column_1)
    plt.ylabel(column_2)

    plt.scatter(x1, y1, c='b')
    plt.scatter(x2, y2, c='o') 
    plt.scatter(x3, y3, c='g')

    plt.show()

showScatterIris(setosa_df, versicolor_df, virginica_df, "Sepal Length", "Sepal Width")
showScatterIris(setosa_df, versicolor_df, virginica_df, "Sepal Length", "Petal Length")
showScatterIris(setosa_df, versicolor_df, virginica_df, "Sepal Length", "Petal Width")
showScatterIris(setosa_df, versicolor_df, virginica_df, "Sepal Width", "Petal Length")
showScatterIris(setosa_df, versicolor_df, virginica_df, "Sepal Width", "Petal Width")
showScatterIris(setosa_df, versicolor_df, virginica_df, "Petal Length", "Petal Width")

# Learning from: https://matplotlib.org/examples/pylab_examples/subplots_demo.html#pylab-examples-subplots-demo



def showHistogramIris(setosa, versicolor, virginica, column_name):
    plt.figure()
    plt.title(column_name)
    plt.xlabel('Centimeters')
    plt.ylabel('Count')
    y1 = setosa[column_name]
    y2 = versicolor[column_name]
    y3 = virginica[column_name]
    plt.hist(y1, bins=12)
    plt.hist(y2, bins=12)
    plt.hist(y3, bins=12)
    plt.show()

showHistogramIris(setosa_df, versicolor_df, virginica_df, "Sepal Length")
showHistogramIris(setosa_df, versicolor_df, virginica_df, "Sepal Width")
showHistogramIris(setosa_df, versicolor_df, virginica_df, "Petal Length")
showHistogramIris(setosa_df, versicolor_df, virginica_df, "Petal Width")




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

