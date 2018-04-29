
# Emma Patton, Programming and Scripting Project - 2018 
# Analysis of Iris Stats Data Set
# The data was investigated using a number of mathematical functions 
# The data has also been grouped and visually represented in histograms and scatter plots 

# Iris Stats Data Data obtained from: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint 

#Research: 
# https://pandas.pydata.org/
# https://matplotlib.org/


# I imported pandas, numpy and matplotlib in order to use built in functions to analyse 
# the data, group it and represent it visually. 


# I first creatd a heading variable and passed a list of strings representing the four
# measurements taken in 

heading = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]

# I then loaded in the data using pd.read_csv()
irisstats = pd.read_csv("data/iris.csv", header = None, names = [*heading, "Species"]) #I needed to add "Species" on to the end of my header so I used the spread operator (*)


irisstats_group_bys = irisstats.groupby(['Species']) #I wanted to separate out nmy data by species so I used the pandas function .groupby 


setosa_df = irisstats_group_bys.get_group('Iris-setosa') #I passed in each group that I wanted using .getgroup 
setosa_df.name = 'Iris-setosa'

versicolor_df = irisstats_group_bys.get_group('Iris-versicolor')
versicolor_df.name = 'Iris-versicolor'

virginica_df = irisstats_group_bys.get_group('Iris-virginica')
virginica_df.name = 'Iris-virginica'


# I then created a function called getIrisStats to analyse each psecies group. I wanted to
# find out the count, mean, median etc. I then printed these individually to the terminal. 

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
    print('') # This information can also be obtained using the built in .describe pandas function 


getIrisStats(setosa_df)
getIrisStats(versicolor_df)
getIrisStats(virginica_df)

# In order to represent my data visually using a scatterplot, I created another function
# called showScatterIris. This allowed me to compare two measurements of each species. 
# Iris Setosa is represented in blue
# Iris Veriscolor is represented in red, and
# Iris Virginica is represented in green. 

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
    plt.scatter(x2, y2, c='r') 
    plt.scatter(x3, y3, c='g')

    plt.show()

showScatterIris(setosa_df, versicolor_df, virginica_df, "Sepal Length", "Sepal Width")
showScatterIris(setosa_df, versicolor_df, virginica_df, "Sepal Length", "Petal Length")
showScatterIris(setosa_df, versicolor_df, virginica_df, "Sepal Length", "Petal Width")
showScatterIris(setosa_df, versicolor_df, virginica_df, "Sepal Width", "Petal Length")
showScatterIris(setosa_df, versicolor_df, virginica_df, "Sepal Width", "Petal Width")
showScatterIris(setosa_df, versicolor_df, virginica_df, "Petal Length", "Petal Width")

# I also investigated the data using the histogram function. I created a function 
# named showHistogramIris. This function allows me to look at one measurement at a time 
# (for example Sepal Length) and allows me to compare each species on a histogram. 

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


# Reading and Research from: 
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
# https://pandas.pydata.org/pandas-docs/stable/visualization.html
# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
# https://matplotlib.org/examples/pylab_examples/subplots_demo.html#pylab-examples-subplots-demo
# https://matplotlib.org/api/colors_api.html 
# https://www.learnpython.org/en/Functions
# https://docs.python.org/3/tutorial/controlflow.html#defining-functions 
