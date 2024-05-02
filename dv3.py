# -*- coding: utf-8 -*-
"""ds_practical_10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TaZDQPFg50-ORgTZ7Ypa4cs7B-uurRMP
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
iris_df = sns.load_dataset('iris')

# Task 1: List down the features and their types
print("Features and their types:")
print(iris_df.dtypes)

# Task 2: Create a histogram for each feature
plt.figure(figsize=(5, 3))
sns.histplot(iris_df['sepal_length'], kde=True)
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 3))
sns.histplot(iris_df['sepal_width'], kde=True)
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 3))
sns.histplot(iris_df['petal_length'], kde=True)
plt.title('Histogram of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 3))
sns.histplot(iris_df['petal_width'], kde=True)
plt.title('Histogram of Petal Width')
plt.xlabel('Petal Width')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Task 3: Create a boxplot for each feature
plt.figure(figsize=(5, 3))
sns.boxplot(data=iris_df, y='sepal_length')
plt.title('Boxplot of Sepal Length')
plt.ylabel('Sepal Length')
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 3))
sns.boxplot(data=iris_df, y='sepal_width')
plt.title('Boxplot of Sepal Width')
plt.ylabel('Sepal Width')
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 3))
sns.boxplot(data=iris_df, y='petal_length')
plt.title('Boxplot of Petal Length')
plt.ylabel('Petal Length')
plt.tight_layout()
plt.show()

plt.figure(figsize=(5, 3))
sns.boxplot(data=iris_df, y='petal_width')
plt.title('Boxplot of Petal Width')
plt.ylabel('Petal Width')
plt.tight_layout()
plt.show()