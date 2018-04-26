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


def getIrisStats(species_group):
    count = species_group.count()
    mean = species_group.mean()
    median = species_group.median()
    stan_dev = species_group.std()
    min = species_group.min(numeric_only=1)
    max = species_group.max(numeric_only=1)

    species_columnwidth = '             {:^12}  {:^12}  {:^12}  {:^12}'
    num_columnwidth = '{:12} {:^12.2f}  {:^12.2f}  {:^12.2f}  {:^12.2f}'

    print(species_group.name)
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


# print(setosa_df.to_html())

# .to_html()













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

