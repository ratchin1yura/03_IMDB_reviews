import glob
import pandas as pd
from tabulate import tabulate

column_name = 'review text'
path = 'Imdb_reviews/test/neg'
df = pd.DataFrame()
new_list = []

for file in glob.glob(path + '**/*.txt', recursive=True):
    with open(file) as f:
        new_line = str(f.readlines())
        new_list.append(new_line)

df1 = pd.Series(new_list)
df2 = pd.concat([df, df1])

look_column = 0
look_text = 'shit'
df3 = df2[df2[look_column].str.contains(look_text)]
print(f'Отзывы, содержащие слово {look_text}')
print(tabulate(df3))
