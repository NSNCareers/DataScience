
import pandas as pd

dt = pd.read_csv("Dir_Pandas/2019 - Copy.csv") 

hd = dt.head() # prints out top five rows by default
tl = dt.tail() # prints out last five rows by default
numberOfRows = dt.head(8)# returns the number of rows passed in as a parameter
shape = dt.shape # prints the number of rows and columns of our data
print(shape)
locate = dt.loc[10:50:2] # For locating rows. start:end:increament

print()