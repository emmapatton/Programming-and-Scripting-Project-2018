# Emma Patton, 2018-04-18
# Getting to know my data and how to manipulate it
# Research and learning from Udacity: https://classroom.udacity.com/courses/ud170


import unicodecsv
import pandas as pd
import numpy as np
from collections import defaultdict 

# with open('data/iris.csv', 'rb') as f:
#     reader = unicodecsv.DictReader(f)
#     irisdata = list(reader)

# print(irisdata)
# This code prints data across the screen aqs a list without clear formatting 

irisstats = pd.read_csv("data/iris.csv", header = None, names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"])

# irisstats.hist()

# plt.show()