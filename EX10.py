import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# For reproducibility
np.random.seed(42)

# Generate synthetic employee dataset
employee_id = range(1, 101)
age = np.random.randint(22, 60, size=100)
gender = np.random.choice(['Male', 'Female'], size=100)
department = np.random.choice(['HR', 'Sales', 'IT', 'Marketing'], size=100)
years_of_experience = np.random.randint(1, 15, size=100)
performance_rating = np.random.randint(1, 6, size=100)
salary = np.random.randint(40000, 120000, size=100)

# Create DataFrame
employee_data = pd.DataFrame({
    'EmployeeID': employee_id,
    'Age': age,
    'Gender': gender,
    'Department': department,
    'Years Of Experience': years_of_experience,
    'Performance Rating': performance_rating,
    'Salary': salary
})

# Save to CSV and reload
employee_data.to_csv('employee_data.csv', index=False)
employee_data = pd.read_csv('employee_data.csv')

# Print outputs
print(employee_data.info())
print(employee_data.describe())
print(employee_data.isnull().sum())

# Department distribution
department_distribution = employee_data['Department'].value_counts()
print(department_distribution)

# Plot: Age distribution
sns.histplot(employee_data['Age'], bins=20, kde=True)
plt.title('Distribution of Employee Ages')
plt.show()

# Plot: Performance Ratings by Department
sns.boxplot(x='Department', y='Performance Rating', data=employee_data)
plt.title('Performance Ratings by Department')
plt.show()
