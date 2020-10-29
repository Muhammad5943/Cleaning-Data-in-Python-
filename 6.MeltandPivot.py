import pandas as pd

df = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/file _csv/data_mp.csv')
tb_melt = pd.melt(frame = df, id_vars = ['country','year'])
print(tb_melt)

tb_melt['sex'] = tb_melt.variable.str[0]
print(tb_melt)