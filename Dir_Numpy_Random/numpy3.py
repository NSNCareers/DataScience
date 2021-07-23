
import  numpy as np 

# Data Types
# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.

# Data Types in Numpy
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string

# Get data type 
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Create an array with data type string:
# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)

# Change data type from integer to boolean:
# arr = np.array([1, 0, 3])
# newarr = arr.astype(bool)
# print(newarr)
# print(newarr.dtype)



