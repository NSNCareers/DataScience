import pandas as pd

dt = pd.read_csv("Dir_Pandas/2019 - Copy.csv",na_values=False)

add_columns = dt['Score'].map(str) + ' ' + dt['GDP per capita'].map(str)
# I converted them into a string
dt['Score_GDP'] = add_columns
scoreGdp = dt['Score_GDP'] # New column added
hd = dt.head(10) 
drop_columns = dt.drop(columns=['Score_GDP','Score'],inplace=True)
# inplace changes or make changes to the data frame
hd = dt.head(10) # Verify columns removed
dt = dt.append({'Country or region':'Maruraji'},ignore_index=True)
# we have to ignore index so as not to throw an erro
tl = dt.tail(10)
filt = dt['Country or region'] == "South Sudan"
drop_rowsOnCondition = dt.drop(index=dt[filt].index)
# Apply condition and get index
drop_rows = dt.drop(index=[156,155], inplace=True)
tl = dt.tail(10)
print()