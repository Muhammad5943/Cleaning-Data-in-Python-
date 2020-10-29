import pandas as pd

state_population = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/merging1.csv')
state_codes = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/merging2.csv')

MergeData = pd.merge(left = state_population, right = state_codes,
                on = None, left_on = 'state', right_on = 'name'
        )

print(MergeData)