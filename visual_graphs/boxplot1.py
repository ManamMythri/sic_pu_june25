
# BOX PLOT
# Problem Statement: Displaying data distribution and outliers using a box plot.
# Question: Which category has the highest spread in the dataset?

# Generate random data for 4 categories



import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module


data = [np.random.randn(100) for _ in range(4)]

# Create box plot
plt.boxplot(data, patch_artist=True)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()