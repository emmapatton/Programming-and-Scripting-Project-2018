# Programming & Scripting Project '18 - Fisher's Iris Data Set

Programming and Scripting Module Project (April 2018) for the online Higher Diploma in Data Analytics with the Galway Mayo Institute of Technology (GMIT). Python is the programming language covered in this module. Visual Studio Code was the editor used to write code for the analysis of the Iris Data Set. 

## Introduction 
Fisher's Iris Data Set [1] is a multivariate data set that was introduced by Ronald Fisher [2], a British statistician and biologist. This data set is extremely well known in classification literature. Fisher introduced the iris data set in his paper "The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis" [3].

The iris data set contains data from 3 different species of iris flower; Iris Setosa, Iris Versicolor and Iris Virginica. Fifty samples of each species were recorded. Four measurements (in centimetres) of each iris flower species were taken; sepal length, sepal width, petal length and petal width [4]. Fisher's data set has been commonly used for learning and testing purposes in areas of computer science and is one of the most well known data sets in this area [5].

## Getting Started
1. Download Python, Anaconda and Visual Studio Code (see links below) as pre-requisites to running this program.
2. All files for this project are available at: https://github.com/emmapatton/Programming-and-Scripting-Project-2018
3. Open the file named: iris_stats_data.py. You can copy the code from this file into Visual Studio Code to run the code.
3. You must also have access to the iris.csv file as this contains the raw data to run the program. 
4. This README provides an overview of investigations of the Iris Data Set. 

### Prerequisites
The following downloads are required to run this program: 
- **Python** 
    - Download Link: https://www.python.org/downloads/
- **Anaconda**
    - Download Link: https://www.anaconda.com/download/
- **Visual Studio Code**
- Download Link: https://code.visualstudio.com/Download


### Iris Data Set Summary
The following three tables provide a basic overview of the iris data set, grouped by species. Each table contains the count, mean, median, standard deviation, minimum and maximum values for sepal length, sepal width, petal length and petal width. 

##### Table 1: 
![alt-text-1](https://github.com/emmapatton/Programming-and-Scripting-Project-2018/blob/master/Iris-Setosa%20Table.PNG)

##### Table 2: 
![alt-text-2](https://github.com/emmapatton/Programming-and-Scripting-Project-2018/blob/master/Iris-Veriscolor%20Table.PNG)

##### Table 3: 
![alt-text-3](https://github.com/emmapatton/Programming-and-Scripting-Project-2018/blob/master/Iris-Virginica%20Table.PNG)

From this initial data, we can see that Iris Virginica has the largest mean for sepal length, petal length and petal width. Iris Virginica however also has higher standard deviation values, indicating a greater spread within the data. Iris Setosa has the smallest minimum values for sepal length, petal length and petal width, coupled with low standard deviations it may be hypothesised that Iris Setosa has the smallest petals of the three species, within this data set. One key difference is that Iris Setosa also has the largest minimum value for sepal width indicating a broad short sepal and short thin petals. Iris Virginica has the largest maximum values for seapl length, petal length and petal width, indicating this in general this species has a larger flower.


Further analysis of the data set is required to provide us with more information. In order to do this I have created scatter plots comparing two measurements of each of the species. A scatter plot [6] is a mathematical diagram that displays two sets of variables. It allows us to visually represent relationships between data. 



##### Figure 1: Scatter Plots 

![alt-text-4](https://github.com/emmapatton/Programming-and-Scripting-Project-2018/blob/master/scatter-all.png)



##### Figure 2: Histograms 

![alt-text-5](https://github.com/emmapatton/Programming-and-Scripting-Project-2018/blob/master/histo-all.png)






5. Write a summary of your investigations.





6. Include supporting tables and graphics as you deem necessary.





## References - need to look at Harvard Referencing (?say why reference is here) 
[1] UC Irvine Machine Learning Repository. Iris data set.
http://archive.ics.uci.edu/ml/datasets/Iris.

[2]Famous Scientists. Information about Ronald Fisher. 
https://www.famousscientists.org/ronald-fisher/

[3] Ronald Fisher's 1936 papere entitled "The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis"
http://rcs.chemometrics.ru/Tutorials/classification/Fisher.pdf

[4] Wikipedia page. Iris Data Set.
https://en.wikipedia.org/wiki/Iris_flower_data_set

[5] https://www.techopedia.com/definition/32880/iris-flower-data-set 25/04/2018 

[6] - http://www.statisticshowto.com/probability-and-statistics/regression-analysis/scatter-plot-chart/ 29/04/2018 







### Project Planning / To do:
- Quality Assurance Framework
- For summary: what the data contains, what it's about, background surrounding data, why it is so commonly used in data analytics
- Write code on the data set:
  - summary statistics
  - max value, min value
  - sum of each column
  - mean/average in each column, median
  - spread within the data, standard deviation
  - think about how to represent visually - histogram, table, scatterplot (research this)
 - Break project into smaller tasks 
 - What does the data look like?
 - Sell Python to colleagues using data set 
 - Explain in README how to run program and what it does 
 - Why is this data set interesting? Can refer to more detailed website that analyses data if further description is needed 
  
### Accessed on 06/04/2018:
- https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python#import research in relation to basic calculations of the data
- https://www.marsja.se/pandas-python-descriptive-statistics/ descriptive stats using pandas
- https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html how to add headers 

### Accessed on 11/04/2018:
- https://matplotlib.org/
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html - accessed for a range of mathematical functions including, mean, min, max, standev etc. 
https://medium.com/@kasiarachuta/basic-statistics-in-pandas-dataframe-594208074f85

### Accessed on 19/04/2018 amd 22/04/2018 
- https://pandas.pydata.org/pandas-docs/stable/groupby.html
- Using pandas to calculate a range of stats for the data

### Accessed on 25/04/2018 
- https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04 
- https://code.visualstudio.com/docs
- https://www.invensis.net/blog/it/benefits-of-python-over-other-programming-languages/

### Accessed on 26/04/2018 
- https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/

### Accessed on 28/04/2018 
- https://matplotlib.org/users/pyplot_tutorial.html#working-with-multiple-figures-and-axes

### Accessed on 29/04/2018 
- https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#images




