import pandas as pd

data = {
    'City': ['Chennai', 'Delhi', 'Chennai', 'Delhi', 'Mumbai', 'Mumbai', 'Delhi', 'Chennai'],
    'Date': ['2024-05-07', '2024-05-14', '2024-06-01', '2024-06-12',
             '2024-06-20', '2024-07-05', '2024-07-15', '2024-07-22'],
    'Temperature': [34, 38, 36, 40, 32, 33, 41, 35]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.month_name()

grouped = df.groupby(['City', 'Month'])['Temperature'].sum().reset_index()

pivot_table = grouped.pivot(index='City', columns='Month', values='Temperature').fillna(0)

summer_months = ['May', 'June', 'July']

pivot_table['Summer_Total'] = pivot_table[summer_months].sum(axis=1)

hottest_city = pivot_table['Summer_Total'].idxmax()

print("Monthly Pivot Table:\n", pivot_table)
print("\nCity with Highest Total Temperature in Summer:", hottest_city)
