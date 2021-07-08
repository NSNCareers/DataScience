import pandas as pd

dt = pd.read_csv("Dir_Pandas/2019 - Copy.csv",na_values=False)

getMedian_gdpPerCapita = dt['GDP per capita'].median() # get median on gdp

get_median = dt.median() # get median on entire data frame

get_describe = dt.describe() # get over view of different statistics of our data
# Run describe on particular column to get more dicrete information
# Count = None missing row (Counts all the non missing values in a column)
get_count = dt['Christians'].value_counts() # Gives you a count on response data on column
get_countpercentage = dt['Christians'].value_counts(normalize=True) # Gets percentage count
get_countByYes = dt['Christians'].value_counts().loc['Yes'] # Returns count of response Yes
get_groupBy = dt.groupby(['Christians'])
get_group = get_groupBy.get_group('Yes') # This will return all data and columns where Christianity is Yes
print(get_countByYes)