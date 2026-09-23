import pandas as pd


# update/add code below ...
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)






def to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary





url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

def task_1():
    df = df_bellevue.copy()
    df["gender"] = df["gender"].replace("u", pd.NA)
    missing_values = df.isna().sum()
    return missing_values.sort_values().index.tolist()

def task_2():
    df = df_bellevue.copy()
    df['date_in'] = pd.to_datetime(df['date_in'])
    df['year'] = df['date_in'].dt.year
    return df.groupby('year').size().reset_index(name='total_admissions')

def task_3():
    return df_bellevue.groupby('gender')['age'].mean()

def task_4():
    return df_bellevue['profession'].value_counts().head(5).index.tolist()