# 📊 EDA Tutorial — Basic Commands

**Author:** Meeta  
**Dataset:** [YouTube Videos Dataset — Kaggle](https://www.kaggle.com/datasets/rajatrc1705/youtube-videos-dataset)  
**Level:** Beginner

---

## What is EDA?

**Exploratory Data Analysis (EDA)** is the first step in any data project.  
Before building models or drawing conclusions, we explore the data to understand:
- What does it look like?
- How big is it?
- Is it clean?
- What are the basic patterns?

This notebook walks through the most essential EDA commands every data analyst uses.

---

## 1. Load the Dataset

We first download the dataset from Kaggle and load it into a **DataFrame**.

> 💡 A DataFrame is like a table in Excel — rows and columns of data.

```python
# kagglehub lets us download datasets directly from Kaggle
import kagglehub

# dataset_download() pulls the dataset and returns the folder path where it's saved
path = kagglehub.dataset_download('rajatrc1705/youtube-videos-dataset')
print(f'Dataset saved at: {path}')
```

```python
# pandas is the most important library for data analysis in Python
import pandas as pd

# read_csv() reads a CSV file and loads it into a DataFrame (df)
# We use the dynamic 'path' variable so this works on any machine
df = pd.read_csv(f'{path}/youtube.csv')

print('Dataset loaded successfully!')
```

## 2. Preview the Data — `df.head()`

Always look at your data before doing anything else.  
`head()` shows the first 5 rows by default.

> 💡 You can pass a number like `df.head(10)` to see more rows.

```python
# Shows the first 5 rows of the DataFrame
# Great for checking column names, data types, and what values look like
df.head()
```

## 3. Count Values in a Column — `value_counts()`

`value_counts()` tells you how many times each unique value appears in a column.  
Here we use it on the `category` column to see which video categories are most common.

> 💡 Results are sorted from most to least frequent automatically.

```python
# df['category'] selects only the category column
# .value_counts() counts how many videos belong to each category
df['category'].value_counts()
```

## 4. Access a Single Cell — `df['column'][index]`

Sometimes you want to look at one specific value — like the title or description of the first video.  
We access it using the column name and the row index number.

> 💡 Index starts at 0 in Python, so the first row is `[0]`.

```python
# Get the title of the first video (row index 0)
# This helps us understand what the text data actually looks like
print('First video title:')
print(df['title'])
```

```python
# Get the description of the first video
# Descriptions can be very long, so we slice only the first 300 characters
# str() converts the value to text safely (in case it's null)
print('First video description (first 300 chars):')
print(str(df['description'])[:300])
```

## 5. Check for Missing Values — `isnull()` and `isna()`

Missing values (also called nulls or NaN) can break your analysis.  
We always check for them early.

> 💡 `isnull()` and `isna()` do exactly the same thing — they are aliases of each other.

```python
# isnull() returns True for each cell that is missing
# .sum() counts the True values per column
# Result: number of missing values in each column
print('Missing values per column:')
df.isnull().sum()
```

```python
# isna() is identical to isnull() — just an alternative name
# Both come from pandas and do the same job
# You can use either one — the result will be the same
print('Same result using isna():')
df.isna().sum()
```

## 6. Check for Duplicate Rows — `duplicated()`

Duplicate rows are rows where every column value is identical.  
They can inflate counts and skew your results, so we remove them.

> 💡 `duplicated().sum()` gives the total count of duplicate rows.

```python
# duplicated() returns True for each row that is an exact copy of a previous row
# .sum() counts how many duplicate rows exist in total
print(f'Number of duplicate rows: {df.duplicated().sum()}')
```

```python
# drop_duplicates() removes all duplicate rows, keeping the first occurrence
df = df.drop_duplicates()

# reset_index() resets the row numbers back to 0, 1, 2...
# drop=True prevents the old index from being saved as a new column
df = df.reset_index(drop=True)

print(f'Rows after removing duplicates: {len(df):,}')
```

## 7. Check Dataset Size & Explore a Column — `shape` and column selection

Finally, we check how many rows remain and explore the titles column.

> 💡 `df.shape` returns `(rows, columns)`. `df.shape[0]` gives just the row count.

```python
# df.shape returns a tuple: (number of rows, number of columns)
#  gives us just the row count
print(f'Total rows in dataset: {df.shape:,}')

# Select the entire 'title' column and store it in a variable
titles = df['title']

# Print all titles
print('\nAll video titles:')
print(titles)
```

## Summary — EDA Commands Cheat Sheet

| Command | What it does |
|---|---|
| `df.head()` | Preview first 5 rows |
| `df['column'].value_counts()` | Count unique values in a column |
| `df['column'][0]` | Access a single cell by index |
| `df.isnull().sum()` | Count missing values per column |
| `df.isna().sum()` | Same as isnull() — alternative name |
| `df.duplicated().sum()` | Count duplicate rows |
| `df.drop_duplicates()` | Remove duplicate rows |
| `df.reset_index(drop=True)` | Reset row numbers after changes |
| `df.shape[0]` | Get total number of rows |

---

*This tutorial is part of Meeta's data analysis portfolio.*
