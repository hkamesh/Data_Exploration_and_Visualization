import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)
start_date = '2020-01-01'
end_date = '2023-12-31'
date_range = pd.date_range(start=start_date, end=end_date, freq='M')
sales_data = np.random.randint(10000, 50000, size=len(date_range))
df = pd.DataFrame({'Date': date_range, 'Sales': sales_data})

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month_name()

sns.set(style="whitegrid")

plt.figure(figsize=(14, 6))
sns.lineplot(data=df, x='Date', y='Sales')
plt.title('Monthly Sales Over Time')
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(df['Sales'], bins=20, kde=True)
plt.title('Distribution of Monthly Sales')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Year', y='Sales')
plt.title('Sales Distribution by Year')
plt.show()

pivot_table = df.pivot_table(values='Sales', index='Month', columns='Year', aggfunc='mean')

months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                'August', 'September', 'October', 'November', 'December']
pivot_table = pivot_table.reindex(months_order)

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt=".0f", cmap='YlGnBu')
plt.title('Average Monthly Sales by Year')
plt.show()
