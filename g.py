import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

pdDataFrame = pd.read_csv("titanic.csv")
print(pdDataFrame.columns)
column = 'age'
new='gender'
pdDataFrame = pdDataFrame.dropna(subset=[column])

mean = pdDataFrame[column].mean()
median = pdDataFrame[column].median()
std = pdDataFrame[column].std()

print(f"Mean of {column}: {mean}")
print(f"Median of {column}: {median}")
print(f"Standard Deviation of {column}: {std}")

plt.figure(figsize=(10, 6))
sb.histplot(pdDataFrame[column], kde=True, bins=20, color='blue')

plt.title(f'Histogram of {column}', fontsize=16)
plt.xlabel(column, fontsize=14)
plt.ylabel('Frequency', fontsize=14)

plt.show()

plt.figure(figsize=(10,6))
sb.hisplot(pdDataFrame[new],kde=True,bins=20,color='red')

plt.title(f'Histogram of {new}', fontsize=16)
plt.xlabel(column,fontsize=14)
plt.ylabel(column,fontsize=14)

plt.show()