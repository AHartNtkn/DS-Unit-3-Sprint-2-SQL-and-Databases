import sqlite3
import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('review', con=conn)

curs = conn.cursor()

print("\nCount how many rows you have - it should be 249!")
query1 = "SELECT COUNT(*) FROM review"
print(curs.execute(query1).fetchone())

print("\nHow many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?")
query2 = "SELECT \"User Id\" FROM review WHERE Nature >= 100 AND Shopping >= 100"
print(curs.execute(query2).fetchall())

print("\nWhat are the average number of reviews for each category?")
query3 = "SELECT AVG(Sports), AVG(Religious), AVG(Nature), AVG(Theatre), AVG(Shopping), AVG(Picnic) FROM review"
print(curs.execute(query3).fetchone())

curs.close()
