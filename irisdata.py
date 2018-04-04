# Emma Patton, 2018-03-02
# Iris data set numerical values printed and formatted
# Data obtained from: http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

heading = ["Petal Length", "Petal Width", "Sepal Length", "Sepal Width"]
columnwidth = '{:^12}  {:^12}  {:^12}  {:^12}'

print(columnwidth.format(*heading))

# Column's formatted to have even spacing following further reading on: https://pyformat.info/ 

with open("data/iris.csv") as f:
    for line in f:
        irisnum = line.split(',')[:4]

        print(columnwidth.format(*irisnum))