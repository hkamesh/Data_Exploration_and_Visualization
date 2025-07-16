import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
data = {
    'ID': range(1, 11),
    'Age': np.random.randint(18, 65, size=10),
    'Income': np.random.randint(30000, 90000, size=10),
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
    'Education': ['High School', 'Bachelor', 'Master', 'PhD', 'Bachelor', 'Master', 'Bachelor', 'PhD', 'High School', 'Master']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display first few rows
print(df.head())

# Summary statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Unique values in categorical columns
print("\nUnique Genders:")
print(df['Gender'].unique())

print("\nUnique Education Levels:")
print(df['Education'].unique())

# Selecting specific columns
selected_columns = df[['Age', 'Income']]
print("\nSelected Columns (Age and Income):")
print(selected_columns.head())

# Filtering: Age > 30
filtered_data = df[df['Age'] > 30]
print("\nFiltered Data (Age > 30):")
print(filtered_data.head())

# Filtering: Male with Master's degree
filtered_rows = df[(df['Gender'] == 'Male') & (df['Education'] == 'Master')]
print("\nFiltered Rows (Male & Master's):")
print(filtered_rows.head())

# Plotting

# Histogram of Age
plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Boxplot of Income
plt.boxplot(df['Income'])
plt.title('Income Distribution')
plt.ylabel('Income')
plt.grid(True)
plt.show()

# Bar chart of Gender distribution
gender_counts = df['Gender'].value_counts()
gender_counts.plot(kind='bar', color='skyblue')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(axis='y')
plt.show()

# Pie chart of Education distribution
education_counts = df['Education'].value_counts()
education_counts.plot(kind='pie', autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightgreen', 'lightskyblue'])
plt.title('Education Distribution')
plt.ylabel('')
plt.show()
