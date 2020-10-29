import pandas as pd

df = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/file _csv/data.csv')
print(df.head())
print('\n')
print(df.tail())
print('\n')
print(df.columns)
print('\n')
print(df.shape)
print('\n')
print(df.info())
