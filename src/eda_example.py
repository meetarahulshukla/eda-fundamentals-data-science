import pandas as pd

# 1. Create a sample dataset with valid arrays
data = {
    'Age': [25, 30, 35, 40, 200],  # 200 is an intentional outlier
    'Salary': [50000, 60000, 70000, 80000, 120000],
    'City': ['New York', 'Paris', 'New York', 'London', 'Paris']
}
df = pd.DataFrame(data)
print(df)

# 2. Data Profiling (Summary Statistics)
print("--- Summary Statistics ---")
print(df.describe())

# 3. Outlier Detection using IQR (For Age)
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
print("\n--- Detected Outliers ---")
print(outliers)

![Jupyter Notebook Run](./images/Screenshot_eda.png)
