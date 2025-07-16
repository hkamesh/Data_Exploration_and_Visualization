import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Employee': ['E101', 'E102', 'E103', 'E104', 'E105', 'E106', 'E107', 'E108', 'E109', 'E110',
                 'E111', 'E112', 'E113', 'E114', 'E115', 'E116', 'E117', 'E118', 'E119', 'E120'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'Sales', 'Sales', 'Marketing', 'Marketing',
                   'IT', 'Finance', 'HR', 'Marketing', 'Sales', 'HR', 'Finance', 'Sales', 'IT', 'Marketing'],
    'Hours_Worked': [40, 50, 45, 38, 42, 55, 48, 44, 35, 40,
                     60, 38, 37, 46, 41, 43, 49, 50, 55, 39]
}

df = pd.DataFrame(data)

dept_summary = df.groupby('Department')['Hours_Worked'].agg(
    Total_Hours='sum',
    Average_Hours='mean',
    Min_Hours='min',
    Max_Hours='max',
    Employee_Count='count'
).reset_index()

pivot_table = dept_summary.set_index('Department')

top_avg_department = pivot_table['Average_Hours'].idxmax()
top_avg_value = pivot_table['Average_Hours'].max()

print("🔹 Department Work Hours Summary Table:\n")
print(pivot_table)
print(f"\n✅ Department with Highest Average Working Hours: {top_avg_department} ({top_avg_value:.2f} hours)")

plt.figure(figsize=(10,6))
plt.bar(pivot_table.index, pivot_table['Average_Hours'], color='skyblue')
plt.axhline(y=top_avg_value, color='red', linestyle='--', label=f'Highest Avg: {top_avg_department}')
plt.title('Average Working Hours by Department')
plt.xlabel('Department')
plt.ylabel('Average Hours Worked')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
