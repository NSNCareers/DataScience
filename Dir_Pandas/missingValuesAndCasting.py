import pandas as pd
import  numpy as np
dt = pd.read_csv("Dir_Pandas/2019 - Copy.csv")

drop_rows = dt.dropna() # This will drop all the rows with no data

drop_rowsWithArg = dt.dropna(axis='columns',how='any') # drop any columns with missing values
# how = all will drop all rows with a missing value
# how = any will drop any
# axis = index will drop only index
# axis = column will drop only columns
drop_rowsWithSubset = dt.dropna(axis='index',how='any',subset=['Population'])
# drop all rows were Population is missing
replace_naData = dt.replace('NA', np.nan, inplace=True) # Replace nan
dt.fillna(0,inplace=True) # Replace na to 0
# inplace will save our changes in the data frame
dataTypes = dt.dtypes # gets data frame data types
mean = dt['Score'].mean() #
# To convert values, use the .astpype(int) function
# If you want to cast a string into an int with missing values,
# it will throw an exception. Always cast to float
# dt.astype(float) will transform all the values in the frame into a float
convert_Score = dt['Score'].astype(int) # convert to int
get_uniqueValues = dt['GDP per capita'].unique() # get unique values
dt.replace('Finland', 'Finish',inplace=True) # Replace data
 
print(dataTypes)
