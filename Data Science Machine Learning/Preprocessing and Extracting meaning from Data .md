> Q1. Which of following is a problem that missing data could cause?

    1. Some visualizations don't 
       work with missing data
    2. Some types of data  
       cleaning steps won't work 
       with null values
    3. Machine learning models 
       will break when they 
       encounter null values
    4. All the above

**Answer :**  Option 2

*Explaination : Visualization represents the remaining values instead of missing values, Machine learning models do work with less accuracy which only means that Data cleaning steps will not work*

> Q2. Select all valid strategies for dealing with null values in a column containing numerical data, assuming that we can't afford to lose any data.

Strategies : <br>

1. Replace missing values with the column median
2. Replace missing values with the column mode
3. Convert the column to categorical format using Coarse Classification ('Binning')
4. Leave the Null values as is.

<br>

    1. Strategy 1 & Strategy 2
    2. Strategy 3 & Strategy 1
    3. Strategy 4 & Strategy 1
    4. Strategy 3 & Strategy 2 

**Answer :**  Option 2

> Q5 Which learning method, algorithm or popular technique commonly used for handling the noise in data mining?

    1. Clustering 
    2. Binning
    3. Regression
    4. All the above

**Answer:**  Option 4

*Explanation : Binning smooths the corrupted data and hence is used to handle noise in data. Other useful techniques to find out noise in data are: clustering method, support vector machine (SVM) algorithm etc.*

> Q6. What happens in clustering method like k-means that is used to handle noise or noisy data in data mining?

    1. Data is organised into clusters
    2. Data is arranged in a line
    3. Any of the above
    4. None of the above

**Answer :** Option 1

*Explanation : The Values lying outside of it are considered as outliers. Thus clusters are made.*

> Q7. What is the difference between a bar chart and a histogram?

    1. Bar charts represent numbers, 
       whereas histograms represent 
       percentages 
    2. A histogram does not show the entire  
       range of scores in a distribution. 
    3. There are no gaps between the bars on 
       a histogram
    4. Bar charts are circular, 
       whereas histograms are square.

**Answer :**  Option 3

*Explanation : Histograms are used to display interval/ratio variables, which involve a continuous range of values, and so there are no gaps between the bars that represent each category.*

> Q8. The worst thing that missing data does is lower sample size and reduce power.

    1. True 
    2. False

**Answer :**  Option 2

*Explanation : If you lose half your sample and have no significant results, you notice.  If the regression coefficients or standard errors aren’t what they’re supposed to be, there’s no way to tell.*

> Q9. Data reduction  is/includes ________

    1. Data-flow diagram show, 
       how data is processed at different stages 
       in the system
    2. registering all/ selected activities of a 
       computer system.
    3. Technique used to transform raw data into 
       a more useful form..
    4. Data is shifted to modern data base 
       management system.

**Answer :** Option 3

*Explanation : In data reduction useless data is removed*

> Q10 Which of the following is not a data pre-processing methods?

    1. Data Visualization
    2. Data Discretization
    3. Data Cleaning 
    4. Data Reduction

**Answer :**  Option 1

*Explanation : Data Visualization is a step after data pre-processing*

*Explanation : While replacing the values in columns we use median not mode so Strategy 1 is fixed. Considering the scenario we cannot leave the null values as it is so Strategy 3 is also fixed so answer will be Option 2*

> Q3. Which of the following code snippets returns a count of the missing values in each column of a DataFrame?

```python
1. some_dataframe.isna().sum()
2. some_dataframe.dropna()
3. some_dataframe.is_na().sum()
4. some_dataframe.value_counts.is_na()
```

**Answer :**  Option 1

*Explanation : some_dataframe.isna() gives null values for each column we just have to use sum to get all the null values*

> Q4. Impact of having noise in data / noisy data?

    1. Increases amount of storage space required 
    2. Decreases amount of storage space required 
    3. No impact on amount of storage space required
    4. None of the above

**Answer :** Option 1
