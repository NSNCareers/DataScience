import numpy as np

# Iterate on the elements of the following 1-D array:
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

# Iterate on each scalar element of the 2-D array:
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)

# The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues 
# which we face in iteration, lets go through it with examples.
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)


# Join two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# Stacking is same as concatenation, 
# the only difference is that stacking is done along a new axis.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# Split the array in 3 parts:
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

# Access the splitted arrays:
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])