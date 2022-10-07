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
