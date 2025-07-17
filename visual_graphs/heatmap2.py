
# SEABORN HEATMAP
# Problem Statement: Understanding correlations between different financial factors.
# Question: Which two variables have the highest positive correlation?

# Compute correlation matrix

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module


data_dict = {
    "total_bill": np.random.uniform(5, 50, 100),
    "tip": np.random.uniform(1, 10, 100),
    "sex": np.random.choice(["Male", "Female"], 100),
    "smoker": np.random.choice(["Yes", "No"], 100),
    "day": np.random.choice(["Thur", "Fri", "Sat", "Sun"], 100),
    "time": np.random.choice(["Lunch", "Dinner"], 100),
    "size": np.random.randint(1, 6, 100)
}

# Convert dictionary to DataFrame
data_df = pd.DataFrame(data_dict)
corr = data_df.select_dtypes(include=np.number).corr()

# Create heatmap with correlation values
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Heatmap")
plt.show()