{
 "nbformat": 4,
 "nbformat_minor": 5,
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10.0"
  }
 },
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": "# \ud83d\udcca EDA Tutorial \u2014 Basic Commands\n\n**Author:** Meeta  \n**Dataset:** [YouTube Videos Dataset \u2014 Kaggle](https://www.kaggle.com/datasets/rajatrc1705/youtube-videos-dataset)  \n**Level:** Beginner  \n\n---\n\n## What is EDA?\n\n**Exploratory Data Analysis (EDA)** is the first step in any data project.\nBefore building models or drawing conclusions, we explore the data to understand:\n- What does it look like?\n- How big is it?\n- Is it clean?\n- What are the basic patterns?\n\nThis notebook walks through the most essential EDA commands every data analyst uses.\n\n---"
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": "## 1. Load the Dataset\n\nWe first download the dataset from Kaggle and load it into a **DataFrame**.\n\n> \ud83d\udca1 A DataFrame is like a table in Excel \u2014 rows and columns of data."
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# kagglehub lets us download datasets directly from Kaggle\nimport kagglehub\n\n# dataset_download() pulls the dataset and returns the folder path where it's saved\npath = kagglehub.dataset_download('rajatrc1705/youtube-videos-dataset')\nprint(f'Dataset saved at: {path}')"
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# pandas is the most important library for data analysis in Python\nimport pandas as pd\n\n# read_csv() reads a CSV file and loads it into a DataFrame (df)\n# We use the dynamic 'path' variable so this works on any machine\ndf = pd.read_csv(f'{path}/youtube.csv')\n\nprint('Dataset loaded successfully!')"
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": "---\n## 2. Preview the Data \u2014 `df.head()`\n\nAlways look at your data before doing anything else.\n`head()` shows the first 5 rows by default.\n\n> \ud83d\udca1 You can pass a number like `df.head(10)` to see more rows."
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# Shows the first 5 rows of the DataFrame\n# Great for checking column names, data types, and what values look like\ndf.head()"
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": "---\n## 3. Count Values in a Column \u2014 `value_counts()`\n\n`value_counts()` tells you how many times each unique value appears in a column.\nHere we use it on the `category` column to see which video categories are most common.\n\n> \ud83d\udca1 Results are sorted from most to least frequent automatically."
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# df['category'] selects only the category column\n# .value_counts() counts how many videos belong to each category\ndf['category'].value_counts()"
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": "---\n## 4. Access a Single Cell \u2014 `df['column'][index]`\n\nSometimes you want to look at one specific value \u2014 like the title or description of the first video.\nWe access it using the column name and the row index number.\n\n> \ud83d\udca1 Index starts at 0 in Python, so the first row is `[0]`."
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# Get the title of the first video (row index 0)\n# This helps us understand what the text data actually looks like\nprint('First video title:')\nprint(df['title'][0])"
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# Get the description of the first video\n# Descriptions can be very long, so we slice only the first 300 characters\n# str() converts the value to text safely (in case it's null)\nprint('First video description (first 300 chars):')\nprint(str(df['description'][0])[:300])"
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": "---\n## 5. Check for Missing Values \u2014 `isnull()` and `isna()`\n\nMissing values (also called nulls or NaN) can break your analysis.\nWe always check for them early.\n\n> \ud83d\udca1 `isnull()` and `isna()` do exactly the same thing \u2014 they are aliases of each other."
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# isnull() returns True for each cell that is missing\n# .sum() counts the True values per column\n# Result: number of missing values in each column\nprint('Missing values per column:')\ndf.isnull().sum()"
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# isna() is identical to isnull() \u2014 just an alternative name\n# Both come from pandas and do the same job\n# You can use either one \u2014 the result will be the same\nprint('Same result using isna():')\ndf.isna().sum()"
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": "---\n## 6. Check for Duplicate Rows \u2014 `duplicated()`\n\nDuplicate rows are rows where every column value is identical.\nThey can inflate counts and skew your results, so we remove them.\n\n> \ud83d\udca1 `duplicated().sum()` gives the total count of duplicate rows."
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# duplicated() returns True for each row that is an exact copy of a previous row\n# .sum() counts how many duplicate rows exist in total\nprint(f'Number of duplicate rows: {df.duplicated().sum()}')"
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# drop_duplicates() removes all duplicate rows, keeping the first occurrence\ndf = df.drop_duplicates()\n\n# reset_index() resets the row numbers back to 0, 1, 2...\n# drop=True prevents the old index from being saved as a new column\ndf = df.reset_index(drop=True)\n\nprint(f'Rows after removing duplicates: {len(df):,}')"
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": "---\n## 7. Check Dataset Size & Explore a Column \u2014 `shape` and column selection\n\nFinally, we check how many rows remain and explore the titles column.\n\n> \ud83d\udca1 `df.shape` returns `(rows, columns)`. `df.shape[0]` gives just the row count."
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": "# df.shape returns a tuple: (number of rows, number of columns)\n# [0] gives us just the row count\nprint(f'Total rows in dataset: {df.shape[0]:,}')\n\n# Select the entire 'title' column and store it in a variable\ntitles = df['title']\n\n# Print all titles\nprint('\\nAll video titles:')\nprint(titles)"
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": "---\n## Summary \u2014 EDA Commands Cheat Sheet\n\n| Command | What it does |\n|---|---|\n| `df.head()` | Preview first 5 rows |\n| `df['column'].value_counts()` | Count unique values in a column |\n| `df['column'][0]` | Access a single cell by index |\n| `df.isnull().sum()` | Count missing values per column |\n| `df.isna().sum()` | Same as isnull() \u2014 alternative name |\n| `df.duplicated().sum()` | Count duplicate rows |\n| `df.drop_duplicates()` | Remove duplicate rows |\n| `df.reset_index(drop=True)` | Reset row numbers after changes |\n| `df.shape[0]` | Get total number of rows |\n\n---\n*This tutorial is part of Meeta's data analysis portfolio.*"
  }
 ]
}