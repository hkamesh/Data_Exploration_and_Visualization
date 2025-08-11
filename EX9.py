import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

data = {
    'fixed acidity': np.random.uniform(5, 15, 100),
    'volatile acidity': np.random.uniform(0.1, 1.5, 100),
    'citric acid': np.random.uniform(0, 1, 100),
    'residual sugar': np.random.uniform(0, 10, 100),
    'alcohol': np.random.uniform(8, 15, 100),
    'quality': np.random.randint(1, 11, 100)
}

wine_df = pd.DataFrame(data)

wine_df.to_csv('wine_quality_dataset.csv', index=False)
wine_df = pd.read_csv('wine_quality_dataset.csv')

print(wine_df.info())
print(wine_df.describe())
print(wine_df.isnull().sum())

sns.countplot(x='quality', data=wine_df)
plt.title('Distribution of Wine Quality')
plt.show()

correlation_matrix = wine_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

selected_features = ['alcohol', 'volatile acidity', 'citric acid', 'residual sugar', 'quality']
sns.pairplot(wine_df[selected_features], hue='quality')
plt.suptitle('Pairplot of Selected Features', y=1.02)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='quality', y='alcohol', data=wine_df)
plt.title('Boxplot of Alcohol Content by Wine Quality')
plt.show()
