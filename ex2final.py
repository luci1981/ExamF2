import pandas as pd
import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    df = pd.read_sql_query('SELECT * FROM core_users', conn)

df['full_name'] = df.first_name + ' ' + df.last_name

#df.to_excel('exercitiu2final.xlsx')

print(df.number_of_login.describe())
print(df.number_of_login.mean)
print(df.number_of_login.std)