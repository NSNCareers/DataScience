
import pandas as pd

dt = pd.read_csv("Dir_Pandas/2019 - Copy.csv") 

hd = dt.head() # prints out top five rows by default
tl = dt.tail() # prints out last five rows by default
numberOfRows = dt.head(8)# returns the number of rows passed in as a parameter
shape = dt.shape # prints the number of rows and columns of our data
print(shape)
locate = dt.loc[10:50:2] # For locating rows. start:end:increament
get_column = dt['Country'] # Get the specified column
get_listOfColumns = dt[['Country','Score']].head(10) #Gets list of columns with 10 rows using head or tail
get_rowsAndColumns = dt.loc[10:20,['Country','Score']] # This will print out rows and columns
filter_rows = dt.loc[dt['Score']<7] # used in filtering rows
filter_specificColumn = dt.loc[dt['Score']>= 7,'Score'] # This will return only score column
filter_usingLambda = dt['Score'].loc[lambda x: x > 6] # Filter using lambda
get_intergerLocation = dt.iloc[:,3].head(5) # Interger location
get_intergerLocations = dt.iloc[1:7,[2,3]] # Here we are printing based on location and not column names
filter_byQuery = dt.query('Score > 7')
dt = dt.rename(columns={'Score':'Scores'}) # Rename specific column
# After renaming, you have to store or save changes in same variable as dt above
# only there after can these changes take effect
renamed_Column = dt['Scores']
filter_byQueryCountry = dt.query('Country == ["Finland","Austria","Denmark","Norway"] & Scores > 7.5') # Query is very importand 
print()