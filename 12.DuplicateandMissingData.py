import pandas as pd

df = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/duplicate_data.csv')
# print(df)

df = df.drop_duplicates()
print(df)

print('\n')

df2 = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/missing_data.csv')
print(df2)
print('\n')
print(df2.info())
print('\n')

df3 = df2.dropna()
print(df3)
print('\n')
# sebelum dirubah NaN menjadi missinf
""" print(df2['sex']) """

# mengubah Nan menjadi missing
df2['sex'] = df2['sex'].fillna('missing')
print(df2['sex'])

print('\n')

# mengubah Nan menjadi angka 0
df2[['total_bill','size']] = df2[['total_bill','size']].fillna(0)
print(df2[['total_bill','size']])

print('\n')
""" 
kegunaan melakukan clean data pada data science adalah untuk mempermudah melakuka perhitungan statistic 
"""

print(df2['total_bill'].mean())
print(df2['total_bill'].median())
print(df2['total_bill'].std())