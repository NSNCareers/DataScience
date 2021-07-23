import numpy as np 

print(np.__version__) # version of numpy

# init array
a = np.array([2,4,6,8,10])

b = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # Nested arrays

print(a.shape) # prints a turple
print(a.dtype) # prints type
print(a.ndim) # prints dimension
print(a.size) # prints size
print(a.itemsize) # prints size in bytes
print(b)