import pandas as pd
# used when found duplicate data
import numpy as np

""" df = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/file _csv/pivot_data.csv')
weather_tidy = df.pivot(index = 'date', columns = 'element', values = 'value')

print(weather_tidy) """

df2 = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/pivot_data2.csv')
# cannot using this code when dupicate value exists
""" weather_tidy2 = df2.pivot(index = 'date', columns = 'element', values = 'value') """
# used it when there are duplicating the data
weather_tidy3 = df2.pivot_table(values = 'value', index = 'date', columns = 'element', aggfunc = np.mean)

print(weather_tidy3)