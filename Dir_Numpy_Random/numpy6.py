
import numpy as np

# Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# Find the indexes where the values are even:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0) # Odd arr%2==1
print(x)

# Find the indexes where the value 7 should be inserted:
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)

# Sort the array:
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

