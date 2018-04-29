# Programming & Scripting Project '18 - Fisher's Iris Data Set

Programming and Scripting Module Project (April 2018) for the online Higher Diploma in Data Analytics with the Galway Mayo Institute of Technology (GMIT). **Python** is the programming language covered in this module. **Visual Studio Code** was the editor used to write code for the analysis of the Data Set. 

## Introduction 
Fisher's Iris Data Set [1] is a multivariate data set that was introduced by Ronald Fisher [2], a British Statistician and Biologist. This data set is extremely well known in classification literature. Fisher introduced the iris data set in his paper "The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis" [3].

The iris data set contains data from 3 different species of iris flower; iris setosa, iris versicolor and iris virginica. Fifty samples of each species were recorded. Four measurements (in centimetres) of each iris flower species were taken; sepal length, sepal width, petal length and petal width [4]. Fisher's data set has been commonly used for learning and testing purposes in areas of computer science and data analytics. It is one of the most well known data sets in this area [5].

## Getting Started
1. Download and install Python and Anaconda (see links below) as pre-requisites to running this program.
2. All files for this project are available at: https://github.com/emmapatton/Programming-and-Scripting-Project-2018
3. Open the terminal or cmd prompt and navigate to the project folder.
4. Run `python iris_stats_data.py`
4. This README provides an overview of investigations of the Iris Data Set. 

### Prerequisites
The following are required to run this program: 
- **Python** 
    - Download Link: https://www.python.org/downloads/
- **Anaconda**
    - Download Link: https://www.anaconda.com/download/


## Iris Data Set Summary
The following three tables provide an initial overview of the iris data set, grouped by species. Each table contains the count, mean, median, standard deviation, minimum and maximum values for sepal length, sepal width, petal length and petal width. 

#### Table 1: 
![alt-text-1](https://github.com/emmapatton/Programming-and-Scripting-Project-2018/blob/master/Iris-Setosa%20Table.PNG)

#### Table 2: 
![alt-text-2](https://github.com/emmapatton/Programming-and-Scripting-Project-2018/blob/master/Iris-Veriscolor%20Table.PNG)

#### Table 3: 
![alt-text-3](https://github.com/emmapatton/Programming-and-Scripting-Project-2018/blob/master/Iris-Virginica%20Table.PNG)

From this initial data, we can see that iris virginica has the largest mean for sepal length, petal length and petal width. Iris virginica however also has higher standard deviation values, indicating a greater spread within the data. Iris setosa has the smallest minimum values for sepal length, petal length and petal width. Coupled with low standard deviations it may be hypothesised that iris setosa has the smallest petals of the three species within this data set. One key difference is that iris setosa also has the largest minimum value for sepal width indicating a broad short sepal and short thin petals. Iris virginica has the largest maximum values for seapl length, petal length and petal width, indicating that in general this species has a larger flower.


Further analysis of the data set is required to provide us with more information. In order to do this I have used histograms. A histogram [8] is a type of bar graph that visually represents the distribution of data. The three species of iris are plotted onto a single histogram, taking into account one variable or measuremeant at a time, for example the first histogram below represents sepal length. 

**Note:** For the histograms: 
- Iris setosa is represented in blue 
- Iris veriscolor is represented in orange 
- Iris virginica is represented in green. 

#### Figure 1: Histograms 

![alt-text-4](https://github.com/emmapatton/Programming-and-Scripting-Project-2018/blob/master/histo-all.png)


In relation to iris setosa, immediately we can see that it's petal length and petal width is much smaller than the other two iris species. There is also less spread within this data. There is overlap between all three species in relation to sepal length and sepal width. Iris setosa has the largest measurements in sepal width and also shows the largest spread of measurements. Iris virginica and iris veriscolor demonstrate the most overlap with iris virginica showing the largest values for sepal length, petal length and petal width. 


Another method of analysising data is through the use of scatter plots, which I have used to compare two measurements of each iris species. A scatter plot [6] is a mathematical diagram that displays two sets of variables. It allows us to visually represent relationships between data. Scatter plots are a useful way of visually representing data as they allow us to look at positive and negative correlation, clusters, groups and outliers [7]. 

**Note:** For the scatter plots: 
- Iris setosa is represented in blue
- Iris veriscolor is represented in red
- Iris virginica is represented in green.

#### Figure 1: Scatter Plots 

![alt-text-5](https://github.com/emmapatton/Programming-and-Scripting-Project-2018/blob/master/scatter-all.png)

From these scatter plots it is immediately obvious that iris setosa (represented by the blue dots) is distinctly separate and therefore different from the other two species of iris. For iris setosa, a positive relationship is noted only between sepal length vs sepal width and petal width vs petal length, as one value increases so does the other value. No other positive correlation is noted in the data sets for iris setosa. An example of an iris setosa outlier can be seen in relation to sepal width vs petal width. 

Overlap between data can be observed for iris virginica (represented by the green dots) and iris versicolor (represented by the red dots) idicating that their measurements are at times similar. There is postive correlation for iris veriscolor and iris virginica in all scatter plots shown, however the spread is variable. Positive correlation is most obvious in these two species groups in relation to sepal length vs petal length  and petal length vs petal width. The larest spread of data is observed in sepal length vs petal width. 


This initial analysis has just scrtached the surface of what data analysis has to offer. The iris data set is particularly interesting as it is useful in providing a practical application for beginning to understand the basics in data analytics, investigating patterns within data and making hypotheses and predictions based on these patterns. Pattern recognition is particularly important in the area of machine learning. If we have a big enough sample size we could, with this data, begin to classify the flower species based on their measurements. 

More detailed analysis and interpretation of the iris data set can be found here: 
- http://rstudio-pubs-static.s3.amazonaws.com/269829_8285925c922e445097f47925b112841f.html
- https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
- https://www.kaggle.com/kamrankausar/iris-dataset-ml-and-deep-learning-from-scratch



## References
[1] UC Irvine Machine Learning Repository. Iris Data Set. [ONLINE] Available at: http://archive.ics.uci.edu/ml/datasets/Iris.[Accessed 06 April 2018].

[2] Famous Scientists. Ronald Fisher. [ONLINE] Available at: https://www.famousscientists.org/ronald-fisher/ [Accessed 06 April 2018].

[3] Fisher, R. A. (1936) The Use of Multiple Measurements in Taxonomic Problems as an Example of Linear Discriminant Analysis. [ONLINE] Available at:http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf [Accessed 06 April 2018].

[4] Wikipedia. is Data Set.[ONLINE] Available at:https://en.wikipedia.org/wiki/Iris_flower_data_set [Accessed 06 April 2018].

[5] Techopedia. Iris Flower Data Set. [ONLINE] Available at: https://www.techopedia.com/definition/32880/iris-flower-data-set [Accessed 25 April 2018]. 

[6]  Statistics How To. Scatter Plot. [ONLINE] Available at: http://www.statisticshowto.com/probability-and-statistics/regression-analysis/scatter-plot-chart/ [Accessed 29 April 2018]. 

[7] Minitab Express Support. Interpret the Key Results for Scatterplot. [ONLINE] Available at: http://support.minitab.com/en-us/minitab-express/1/help-and-how-to/graphs/scatterplot/interpret-the-results/key-results/ [Accessed 29 April 2018]. 

[8] LEARD Statistics. Histograms. [ONLINE] Available at: https://statistics.laerd.com/statistical-guides/understanding-histograms.php [Accessed 29 April 2018]. 



## Bibliography 
- Data Camp. Python Exploratory Data Analysis Tutorial. [ONLINE] Available at: https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python#import [Accessed 06 April 2018]. 

- Erik Marsja. Descriptive Statistics using Python. [ONLINE] Available at: https://www.marsja.se/pandas-python-descriptive-statistics/ [Accessed 06 April 2018].  

- Pandas 0.22.0 Documentation. pandas.read_csv. [ONLINE] Available at: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html [Accessed 06 April 2018].  

- Matplotlib. [ONLINE] Available at: https://matplotlib.org/ [Accessed 11 April 2018]. 

- Pandas 0.22.0 Documentation. Pandas.DataFrame. [ONLINE] Available at: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html [Accessed 11 April 2018]. 

- Medium. Basic Statistics in Pandas DataFrame. [ONLINE] Available at: https://medium.com/@kasiarachuta/basic-statistics-in-pandas-dataframe-594208074f85 [Accessed 11 April 2018]. 

- Learn Python. Functions. [ONLINE] Available at: https://www.learnpython.org/en/Functions [Accessed 11 April 2018]. 

- Python. Defining Functions. [ONLINE] Available at: https://docs.python.org/3/tutorial/controlflow.html#defining-functions [Accessed 11 April 2018].  

- Pandas 0.22.0 Documentation. Group By: Split-Apply-Combine. [ONLINE] Available at: ¶https://pandas.pydata.org/pandas-docs/stable/groupby.html [Accessed 19 April 2018]. 

- Invensis. Benefits of Python over Other Programming Languages. [ONLINE] Available at: https://www.invensis.net/blog/it/benefits-of-python-over-other-programming-languages/ [Accessed 25 April 2018]. 

- Shane Lynn. The Pandas DataFrame – Loading, Editing, and Viewing Data in Python. [ONLINE] Available at: https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/ [Accessed 26 April 2018]. 

- Matplotlib. Pyplot Tutorial. [ONLINE] Available at: https://matplotlib.org/users/pyplot_tutorial.html#working-with-multiple-figures-and-axes [Accessed 28 April 2018]. 

- GitHub Help. Basic Writing and Formatting Syntax. [ONLINE] Available at: https://help.github.com/articles/basic-writing-and-formatting-syntax/ [Accessed 29 April 2018]. 

- Case Study: IRIS Classification. [ONLINE] Available at: http://rstudio-pubs-static.s3.amazonaws.com/269829_8285925c922e445097f47925b112841f.html [Accessed 29 April 2018]. 

- Kaggle. Machine Learning with Iris Dataset. [ONLINE] Available at: https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset [Accessed 29 April 2018].

- Kaggle. Iris Dataset ML and Deep Learning from Scratch. [ONLINE] Available at: https://www.kaggle.com/kamrankausar/iris-dataset-ml-and-deep-learning-from-scratch [Accessed 29 April 2018].

