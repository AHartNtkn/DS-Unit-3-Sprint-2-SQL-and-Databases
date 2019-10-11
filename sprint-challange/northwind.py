import sqlite3

# Connect to database and connect cursor
sl_conn = sqlite3.connect('northwind_small.sqlite3')
sl_curs = sl_conn.cursor()

# What are the ten most expensive items (per unit price) in the database?
sql_comm_3 = """
SELECT ProductName, UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""
print("Ten most expensive items: ", sl_curs.execute(sql_comm_3).fetchall())

# What is the average age of an employee at the time of their hiring? 
sql_comm_4 = """
SELECT AVG(HireDate - BirthDate)
FROM Employee
"""
print("Average employee age: ", sl_curs.execute(sql_comm_4).fetchall())

# How does the average age of employee at hire vary by city?
sql_comm_5 = """
SELECT City, AVG(HireDate - BirthDate)
FROM Employee
GROUP BY City
"""
print("Average employee age by city: ",
      sl_curs.execute(sql_comm_5).fetchall())

# Close cursor and connection
sl_curs.close()
sl_conn.close()
