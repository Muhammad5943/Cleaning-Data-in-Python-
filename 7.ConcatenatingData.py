import pandas as pd

weather_p1 = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/file _csv/concat1.csv')
weather_p2 = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/file _csv/concat2.csv')

concetenated = pd.concat([weather_p1, weather_p2])
# print(conceteneted)

""" kesalahan yang terjadi jika langsung concated adalah di index yang sama, jadi agar
dapat mendapatkan index yang berbeda """

# contoh index yang didapat ketika ada kesalahan concat
concetenated = concetenated.loc[0,:]
# print(concetenated)

concatenated = pd.concat([weather_p1, weather_p2], ignore_index = True)
print(concatenated)