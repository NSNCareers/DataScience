
import matplotlib.pyplot as plt
import seaborn as sns


# Plotting a Displot
# sns.histplot([0, 1, 2, 3, 4, 5])
sns.distplot([0, 1, 2, 3, 4, 5]) # depricated
# plt.show()

# Plotting a Distplot Without the Histogram
sns.distplot([0, 1, 2, 3, 4, 5], hist=False) # depricated
#sns.kdeplot([0, 1, 2, 3, 4, 5], hist=False)
plt.show()
