
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# Exponential distribution is used for describing time till next event e.g. failure/success etc.
# It has two parameters:
# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
# size - The shape of the returned array.


# Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:
x = random.exponential(scale=2, size=(2, 3))
# print(x)


# Visualization of Exponential Distribution
sns.distplot(random.exponential(size=1000), hist=False)
# plt.show()