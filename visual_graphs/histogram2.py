
# HISTOGRAM
# Problem Statement: Analyzing the frequency distribution of normally distributed data.
# Question: How is the data distributed across different bins?

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module


# Generate normally distributed random data
data = np.random.randn(1000)

# Create histogram with 30 bins
plt.hist(data, bins=30, color='green', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
