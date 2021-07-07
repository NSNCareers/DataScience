import pandas as pd

dt = pd.read_csv("Dir_Pandas/2019 - Copy.csv",na_values=False)

sort_byCounntry = dt.sort_values(by='Country or region') # Places Column in alphabetical
sort_byCounntryAscending = dt.sort_values(by='Country or region',ascending=False) # Descending Order
sort_withIndex = dt.sort_index() # Sort with Index
sort_singleColumn = dt['Score'].sort_values() # Sort only score
sort_byLargest = dt['Score'].nlargest(10) # 10 largest score
sort_allLargest = dt.nlargest(10,'Score') # 10 largest scores but all columns
# To get smallest use nsmallest() function

print()