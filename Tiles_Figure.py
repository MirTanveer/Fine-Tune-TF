import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm

# Data
data = {
    "": ["ESM2_8M", "ESM2_8M*", "ESM2_35M", "ESM2_35M*", "ESM2_150M", "ESM2_150M*", "ESM2_650M", "ESM2_650M*"],
    "Acc": [6.21, 4.33, 3.85, 3.42, 2.06, 1.48, 1.99, 1.14],
    "Sn": [3.79, 0.51, 1.13, 1.03, 4.03, 0.92, 4.74, 1.48],
    "Sp": [8.81, 8.15, 6.6, 5.72, -0.94, 1.94, -1.25, 0.70],
    "MCC": [14.61, 8.47, 8.52, 6.65, 4.75, 3.76, 8.16, 5.58],
    "AUC": [1.00, -0.15, 0.18, -0.70, 0.43, -0.92, 0.81, 0.61],
    "F1": [5.82, 3.85, 6.57, 5.70, 2.26, 1.89, 3.68, 2.72]
}

df = pd.DataFrame(data)
df.set_index("", inplace=True)

# Transpose the dataframe to swap rows and columns
df_t = df.T

# Define colors for ranges
colors = ["#d3d3d3", "#fff7bc", "#add8e6"]  # negative, 0-2, >2
cmap = ListedColormap(colors)

# Define boundaries for color mapping
bounds = [-np.inf, 0, 2, np.inf]  # negative <0, 0–2, >2
norm = BoundaryNorm(bounds, cmap.N)

plt.figure(figsize=(6, 5))  # Adjust figure size for transposed data
ax = sns.heatmap(df_t, annot=True, fmt=".2f", cmap=cmap, norm=norm, cbar=False, linewidths=0.5, square=True)

# Set horizontal y-axis tick labels (row names)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=10)
# Set horizontal x-axis tick labels (column names)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=10)

plt.title("Improvement in the Fine-tuned and LoRA models over \n Pre-trained models")
plt.tight_layout()
plt.savefig('Heatmap_fine_tuning_and LoRA_models.png', dpi=400)  # Save the figure
plt.show()
