import seaborn as sns
import pandas as pd

# update/add code below ...
def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2) #doing the recursive calculation

def to_binary(n):
    """Convert a decimal number to its binary representation."""
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary # converting to binary
        n = n // 2 # integer division
    return binary

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1():
    """Task 1: Identify columns with the most missing values."""
    df = df_bellevue.copy()
    df["gender"] = df["gender"].replace(["?", "g", "h"], pd.NA) #Replacing the values
    missing_values = df.isna().sum()# Counting missing values
    return missing_values.sort_values(kind="stable").index.tolist()# Returning the column names with the most missing values
    
def task_2():
    """Task 2: Count admissions by year."""
    df = df_bellevue.copy()
    df['date_in'] = pd.to_datetime(df['date_in']) # Converting to datetime
    df['year'] = df['date_in'].dt.year # Extracting year
    return df.groupby('year').size().reset_index(name='total_admissions')# Counting admissions by year

def task_3():
    """Task 3: Calculate the average age by gender."""
    return df_bellevue.groupby('gender')['age'].mean()# Calculating average age by gender

def task_4():
    """Task 4: Identify the top 5 professions."""
    return df_bellevue['profession'].value_counts().head(5).index.tolist()# Identifying the top 5 professions