import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/file _csv/data.csv')
# print(df.info())

df['population'] = df.population.str.replace(',','').astype('float')
print(df.info())
print('\n')
print(df.describe())

print('\n')
print(df[df.population > 1000000000])

# Show hiatogram
df.population.plot(kind = 'hist')
# plt.show()

df.boxplot(column = 'population', by = 'Continent')
plt.show()
