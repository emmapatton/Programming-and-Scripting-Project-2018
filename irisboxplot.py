# Emma Patton, 2018-04-26
# Boxplot of Iris Data Set

# Research from: https://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html#box-plots

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


irisstats = pd.read_csv("data/iris.csv", header = None, names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"])





