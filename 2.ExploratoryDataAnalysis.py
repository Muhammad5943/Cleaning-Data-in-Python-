import pandas as pd

df = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/file _csv/data.csv')

# menampilkan informasi data
print(df.info())

# spasi
print('\n')

# mencari nilai data yang hilang (cara1)
print(df.Continent.value_counts(dropna = False))

# spasi
print('\n')

# mencari nilai data yang hilang (cara2)
print(df['Continent'].value_counts(dropna = False))

# spasi
print('\n')

# mencari nilai top 5 (head) dari data (country)
print(df['Country'].value_counts(dropna = False).head())

# spasi
print('\n')

# mencari nilai dari fertility
print(df.fertility.value_counts(dropna = False).head())

# spasi
print('\n')

# mencari nilai dari population
print(df.population.value_counts(dropna = False).head())

# spasi
print('\n')

print(df.describe())