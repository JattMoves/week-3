import pandas as pd


# update/add code below ...
def sum_fibonacci(n):
    if n <=0:
        return 0
    elif n==1:
        return 0
    
    a,b = 0, 1
    total = 2
    for _ in range(3,n):
        a, b = b, a + b
        total += b
        
    return total





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
    df['gender'] = df['gender'].replace('u',pd.NA)
    return df.isna().sum().sort_values(ascending=True).index.sort_values().tolist()

def task_2():
    df = df_bellevue.copy()
    df['date_in'] = pd.to_datetime(df['date_in'])
    df['year'] = df['date_in'].dt.year
    return df.groupby('year').size().reset_index(name='total_admissions')

def task_3():
    return df_bellevue.groupby('gender')['age'].mean()

def task_4():
    return df_bellevue['profession'].value_counts().head(5).index.tolist()