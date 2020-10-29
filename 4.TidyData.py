import pandas as pd

df = pd.read_csv('/home/muhammad/apps/Learn_python/Cleaning Data in Python/file _csv/tidy_data.csv')
tidyData = pd.melt(frame = df, id_vars = 'name', value_vars = ['treatment a', 'treatment b'],
                    var_name = 'treatment', value_name = 'result'
                )

print(tidyData)