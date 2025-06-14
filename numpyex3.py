# Part 1: NumPy Arrays
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # for advanced plots

# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Array operations
print("Original Array:", arr1)
print("Array + 5:", arr1 + 5)
print("Sliced Array:", arr1[1:4])
print("Reshaped 2D Array:\n", arr2.reshape(3, 2))

# Part 2: Pandas DataFrame
data = {
    'Name': ['Kamesh', 'Lokan', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 88]
}
df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)
print("\nDataFrame Info:")
print(df.info())
print("\nStatistics:")
print(df.describe())

# Part 3: Matplotlib Plots

# Line Plot
plt.figure()
plt.plot(df['Name'], df['Score'], marker='o')
plt.title('Scores of Students')
plt.xlabel('Name')
plt.ylabel('Score')
plt.grid(True)
plt.show()

# Bar Plot
plt.figure()
plt.bar(df['Name'], df['Age'], color='orange')
plt.title('Age of Students')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()

# Pie Chart
plt.figure()
plt.pie(df['Score'], labels=df['Name'], autopct='%1.1f%%', startangle=90)
plt.title('Score Distribution')
plt.show()

# Additional Data Visualization Techniques

# Scatter Plot (Age vs Score)
plt.figure()
plt.scatter(df['Age'], df['Score'], color='green')
for i, name in enumerate(df['Name']):
    plt.text(df['Age'][i]+0.3, df['Score'][i], name)
plt.title('Scatter Plot of Age vs Score')
plt.xlabel('Age')
plt.ylabel('Score')
plt.grid(True)
plt.show()

# Histogram of Age
plt.figure()
plt.hist(df['Age'], bins=5, color='purple', alpha=0.7)
plt.title('Histogram of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Box Plot for Score
plt.figure()
plt.boxplot(df['Score'])
plt.title('Box Plot of Scores')
plt.ylabel('Score')
plt.show()

# Violin Plot (requires seaborn)
plt.figure()
sns.violinplot(data=df[['Age', 'Score']])
plt.title('Violin Plot of Age and Score')
plt.show()

# Heatmap of correlation matrix
plt.figure()
corr = df[['Age', 'Score']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Area Plot (Age and Score)
plt.figure()
df.set_index('Name')[['Age', 'Score']].plot.area(alpha=0.4)
plt.title('Area Plot of Age and Score')
plt.ylabel('Value')
plt.xlabel('Name')
plt.show()

# Step Plot (Score)
plt.figure()
plt.step(df['Name'], df['Score'], where='mid', color='red')
plt.title('Step Plot of Scores')
plt.xlabel('Name')
plt.ylabel('Score')
plt.show()

# KDE Plot (Kernel Density Estimate) - for numeric columns
plt.figure()
sns.kdeplot(df['Age'], shade=True, color='blue', label='Age')
sns.kdeplot(df['Score'], shade=True, color='red', label='Score')
plt.title('KDE Plot for Age and Score')
plt.legend()
plt.show()
