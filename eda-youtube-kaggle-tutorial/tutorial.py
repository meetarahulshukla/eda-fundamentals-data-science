# kagglehub lets us download datasets directly from Kaggle
import kagglehub

# dataset_download() pulls the dataset and returns the folder path where it's saved
path = kagglehub.dataset_download('rajatrc1705/youtube-videos-dataset')
print(f'Dataset saved at: {path}')

# pandas is the most important library for data analysis in Python
import pandas as pd

# read_csv() reads a CSV file and loads it into a DataFrame (df)
# We use the dynamic 'path' variable so this works on any machine
df = pd.read_csv(f'{path}/youtube.csv')

print('Dataset loaded successfully!')

# Shows the first 5 rows of the DataFrame
# Great for checking column names, data types, and what values look like
df.head()

# df['category'] selects only the category column
# .value_counts() counts how many videos belong to each category
df['category'].value_counts()

# Get the title of the first video (row index 0)
# This helps us understand what the text data actually looks like
print('First video title:')
print(df['title'][0])

# Get the description of the first video
# Descriptions can be very long, so we slice only the first 300 characters
# str() converts the value to text safely (in case it's null)
print('First video description (first 300 chars):')
print(str(df['description'][0])[:300])

# isnull() returns True for each cell that is missing
# .sum() counts the True values per column
# Result: number of missing values in each column
print('Missing values per column:')
df.isnull().sum()

# isna() is identical to isnull() — just an alternative name
# Both come from pandas and do the same job
# You can use either one — the result will be the same
print('Same result using isna():')
df.isna().sum()

# duplicated() returns True for each row that is an exact copy of a previous row
# .sum() counts how many duplicate rows exist in total
print(f'Number of duplicate rows: {df.duplicated().sum()}')

# drop_duplicates() removes all duplicate rows, keeping the first occurrence
df = df.drop_duplicates()

# reset_index() resets the row numbers back to 0, 1, 2...
# drop=True prevents the old index from being saved as a new column
df = df.reset_index(drop=True)

print(f'Rows after removing duplicates: {len(df):,}')

# df.shape returns a tuple: (number of rows, number of columns)
# [0] gives us just the row count
print(f'Total rows in dataset: {df.shape[0]:,}')

# Select the entire 'title' column and store it in a variable
titles = df['title']

# Print all titles
print('\nAll video titles:')
print(titles)
