
# VIOLIN PLOT
# Problem Statement: Comparing multiple distributions using a violin plot.
# Question: How does the density of data differ across categories?

# Create violin plot

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

data = [np.random.randn(100) for _ in range(4)]
plt.violinplot(data)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Violin Plot")
plt.show()