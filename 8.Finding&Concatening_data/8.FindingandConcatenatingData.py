import glob
import pandas as pd

pattern = '*.csv'
# pattern = 'uber-raw-data-2014_04.csv, uber-raw-data-2014_06.csv, uber-raw-data-2014_06.csv'
csv_files = glob.glob(pattern)

print(csv_files)

csv2 = pd.read_csv(csv_files[0])
head = csv2.head()

# print(head)

list_data = []
for filename in csv_files:
    data = pd.read_csv(filename)
    list_data.append(data)
    
showConcat = pd.concat(list_data)
print(showConcat)