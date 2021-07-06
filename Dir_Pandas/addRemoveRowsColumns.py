import pandas as pd

dt = pd.read_csv("Dir_Pandas/2019 - Copy.csv",na_values=False)

add_columns = dt['Score'] + '' + dt['GDP per capita']

print()