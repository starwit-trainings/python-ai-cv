import pandas as pd

# Load data from a CSV file
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataframe
print("First 5 rows of the dataset:")
print(df.head())

# Display basic statistics about the dataframe
print("\nBasic statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Add a new column: tip percentage
df['tip_pct'] = df['tip'] / df['total_bill'] * 100
print("\nDataset with tip percentage added:")
print(df.head())

# Group by day and calculate the average tip percentage
avg_tip_pct_by_day = df.groupby('day')['tip_pct'].mean()
print("\nAverage tip percentage by day:")
print(avg_tip_pct_by_day)

# Pivot table: average total bill and tip by day and time
pivot_table = df.pivot_table(values=['total_bill', 'tip'], index='day', columns='time', aggfunc='mean')
print("\nPivot table of average total bill and tip by day and time:")
print(pivot_table)

# Filter rows: only records where tip percentage is greater than 20%
high_tippers = df[df['tip_pct'] > 20]
print("\nRows where tip percentage is greater than 20%:")
print(high_tippers.head())

# Sorting the dataframe by total bill
sorted_df = df.sort_values(by='total_bill', ascending=False)
print("\nData sorted by total bill (descending):")
print(sorted_df.head())

# Basic plotting with pandas
import matplotlib.pyplot as plt

# Plot total bill vs tip
plt.figure(figsize=(10, 6))
plt.scatter(df['total_bill'], df['tip'])
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# Plot average tip percentage by day
plt.figure(figsize=(10, 6))
avg_tip_pct_by_day.plot(kind='bar')
plt.title('Average Tip Percentage by Day')
plt.xlabel('Day')
plt.ylabel('Tip Percentage')
plt.show()