#!/usr/bin/env python

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load a sample dataset
tips = sns.load_dataset("tips")

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Example 1: Scatter plot with regression line
plt.figure(figsize=(10, 6))
sns.lmplot(x="total_bill", y="tip", data=tips)
plt.title("Scatter plot with regression line")
plt.show()

# Example 2: Box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Box plot of total bill by day")
plt.show()

# Example 3: Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)
plt.title("Violin plot of total bill by day and sex")
plt.show()

# Example 4: Heatmap
flights = sns.load_dataset("flights")
flights_pivot = flights.pivot("month", "year", "passengers")

plt.figure(figsize=(12, 8))
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Heatmap of flights data")
plt.show()

# Example 5: Pair plot
plt.figure(figsize=(10, 10))
sns.pairplot(tips, hue="sex")
plt.suptitle("Pair plot of tips dataset", y=1.02)
plt.show()

# Example 6: Distribution plot
plt.figure(figsize=(10, 6))
sns.histplot(tips["total_bill"], kde=True)
plt.title("Distribution plot of total bill")
plt.show()

# Example 7: Joint plot
plt.figure(figsize=(10, 10))
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex", color="purple")
plt.suptitle("Joint plot of total bill and tip", y=1.02)
plt.show()

# Example 8: Cat plot
plt.figure(figsize=(10, 6))
sns.catplot(x="day", y="total_bill", hue="smoker", kind="swarm", data=tips)
plt.title("Cat plot of total bill by day and smoker status")
plt.show()