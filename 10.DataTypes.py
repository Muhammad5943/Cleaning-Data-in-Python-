import pandas as pd 

# data type in every columns is object and int64 on 'treatment b'
df = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/data_types.csv')
print(df.dtypes)

print('\n')

# change data type for 'treatment b' to string/ object, and data type 'sex' to category
df['treatment b'] = df['treatment b'].astype(str)
df['sex'] = df['sex'].astype('category')
print(df.dtypes)

print('\n')

# change data typr on 'treatment a' to float64
df['treatment a'] = pd.to_numeric(df['treatment a'], errors = 'coerce')
print(df.dtypes)

# to check value in the column
print('\n')
print(df['treatment a'])
print('\n')
print(df['treatment b'])
print('\n')
print(df['sex'])