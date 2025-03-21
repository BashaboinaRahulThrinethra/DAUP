# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OUogcGOGKUiuuEdyYP8dcdtBXboo99dT
"""

import pandas as pd
from scipy.stats import skew, kurtosis

df = pd.read_csv('/content/Bank-Customer-Attrition-Insights-Data.csv')

df.head()

numerical_vars = ['Balance', 'CreditScore', 'EstimatedSalary']

# Calculate summary statistics for each variable
for var in numerical_vars:
    mean = df[var].mean()
    median = df[var].median()
    std_dev = df[var].std()
    skewness = skew(df[var])
    kurtosis_val = kurtosis(df[var])

    print(f"Summary statistics for {var}:")
    print(f"  Mean: {mean}")
    print(f"  Median: {median}")
    print(f"  Standard Deviation: {std_dev}")
    print(f"  Skewness: {skewness}")
    print(f"  Kurtosis: {kurtosis_val}")
    print("\n")

gender_distribution = df['Gender'].value_counts(normalize=True) * 100
print("Distribution by Gender:")
print(gender_distribution)

geography_distribution = df['Geography'].value_counts(normalize=True) * 100
print("\nDistribution by Geography:")
print(geography_distribution)

age_distribution = df['Age'].value_counts(bins=10, normalize=True) * 100 # Or use 'AgeGroup' if created
print("\nDistribution by Age:")
print(age_distribution)

# Calculate minimum, maximum, and average estimated salary for active vs. inactive customers
salary_stats = df.groupby('IsActiveMember')['EstimatedSalary'].agg(['min', 'max', 'mean'])

# Display the results
print(salary_stats)

correlation_matrix = df[['CreditScore', 'Balance', 'EstimatedSalary']].corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

import matplotlib.pyplot as plt
import seaborn as sns

# Create a heatmap
plt.figure(figsize=(8, 6))  # Adjust figure size if needed
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Group data by 'Exited' status
grouped_data = df.groupby('Exited')

# Calculate average balance for each group
average_balance = grouped_data['Balance'].mean()

# Display the results
print("Average Balance:")
print(average_balance)

churn_stats = df.groupby('Exited')[['Balance', 'EstimatedSalary']].agg(['mean', 'median', 'std'])
print(churn_stats)

import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x='Exited', y='Balance', data=df)
plt.title('Balance Distribution by Churn Status')
plt.show()

low_credit_score_threshold = 650
high_balance_threshold = 10000

filtered_df = df[(df['CreditScore'] < low_credit_score_threshold) & (df['Balance'] > high_balance_threshold)]

# Calculate the probability
probability = len(filtered_df) / len(df)

# Print the result
print(f"Probability of low credit score and high balance: {probability}")