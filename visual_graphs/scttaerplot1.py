
# SCATTER PLOT
# Problem Statement: Understanding the correlation between two variables.
# Question: What pattern can we observe in the scatter plot of randomly generated values?

# Generate 50 random values for x and y
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

x = np.random.rand(50)
y = np.random.rand(50)

# Create scatter plot
plt.scatter(x, y, color='red', marker='o')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")
plt.show()