import numpy as np


# Make a copy, change the original array, and display both arrays:
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)

# Make a view, change the original array, and display both arrays:
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)

# Print the value of the base attribute to check if an array owns it's data or not:
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# y = arr.view()
# print(x.base)
# print(y.base)

# Print the shape of a 2-D array:
# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr.shape)

# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('shape of array :', arr.shape)

# Convert the following 1-D array with 12 elements into a 2-D array.
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)