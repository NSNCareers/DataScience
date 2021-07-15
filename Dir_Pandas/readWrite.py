import pandas as pd
dt = pd.read_csv("Dir_Pandas/2019 - Copy.csv",na_values=False)

# Writting in files using Python build in liabrary
f = open('Dir_Pandas/2019 - Copy.csv','r')
f.close() # To avoid memory leaks
# r = read
# w = write
# a = append

# Using Context manager
with open('Dir_Pandas/2019 - Copy.csv','r') as f:
    # file_Contents = f.read() # For small files
    file_Contents = f.readlines() # Returns a list
    # file_Contents = f.readline() # returns each line
    print(file_Contents)
    
# Creating and mordifying new files

# Export to new file
filt = (dt['Country or region']== 'Denmark')
senegal_dt = dt.loc[filt]
modified_excel = dt.to_csv('Dir_Pandas/2019Modified - Copy.csv')
# Export json
modified_json = dt.to_json('Dir_Pandas/2019Modified - .json',orient='records', lines = True)

# Reading csv files using Pandas
skip_rows = pd.read_csv("Dir_Pandas/2019 - Copy.csv",skiprows = 3) # Skip rows
set_headers = pd.read_csv("Dir_Pandas/2019 - Copy.csv", header = None, names=["Sequence", "Start", "End", "Coverage"]) # Set new headers
skip_rows = pd.read_csv("Dir_Pandas/2019 - Copy.csv", nrows = 4) # Read just 4 rows
dt_na = pd.read_csv("Dir_Pandas/2019 - Copy.csv",na_values = False) # clean up by replacing all na cells

# Apply is used for calling a function on values
# Apply only works for a series
get_rowLength = dt['Country or region'].apply(len) # Gets the length of each row

def update_countryOrRegion1(country):
    return country.upper()

def update_countryOrRegion2(country):
    if country == 'Denmark':
        return country.replace('Denmark','Zimbabwe')

def update_countryOrRegion3(country):
    if country == 'Denmark':
        return country.strip('Den')

def update_country(country):
    if country == 'Finland is very cold':
        return country.replace('is very cold','')
    else:
        return country

def updateRow(country):
    if '#' in country:
        return country.replace('#','')
    else:
        return country

# Check bool result
boolResult = dt['Country or region'].str.contains('Finland')
# To update dataframe, put in new column
dt['Countries'] = dt['Country or region'].apply(updateRow)
# update_cellContent1 = dt['Country or region'].apply(lambda x : x.lower())
dt['country'] = dt['Country or region'].apply(lambda x: x.replace('is very cold','') if x=='Finland is very cold' else x)
# update_cellContent2 = dt['Country or region'].apply(update_countryOrRegion2)
# update_cellContent3 = dt['Country or region'].apply(update_countryOrRegion3)

# Applymap works for the entire dataframe
# get_allRowLength = dt.applymap(len) # If all your columns are strings

# Map only works for a series
dt['Map'] = dt['Country or region'].map({'Denmark':'DDK','Germany':'Euro'}) # mapps with nan values
dt['Replace'] = dt['Country or region'].replace({'Denmark':'DDK','Germany':'Euro'})

# Rename
dt.rename(columns = {'Country or region':'Country'}, inplace = True)
print()