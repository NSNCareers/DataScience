
import numpy as np

# How To Create Your Own ufunc
# To create you own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

# The frompyfunc() method takes the following arguments:

# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.
# Example
# Create your own ufunc for addition:

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)
# print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))


# Check if a Function is a ufunc
# Check the type of a function to check if it is a ufunc or not.

# A ufunc should return <class 'numpy.ufunc'>.

# Check if a function is a ufunc:
# print(type(np.add))

# Use an if statement to check if the function is a ufunc or not:
if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')