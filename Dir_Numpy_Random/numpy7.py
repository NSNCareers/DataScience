
from numpy import random
import numpy as np

# Generate a random integer from 0 to 100:
x = random.randint(100)
print(x)

# Generate a 1-D array containing 5 random integers from 0 to 100:
x=random.randint(100, size=(5))
print(x)

# Randomly shuffle elements of following array:
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)



