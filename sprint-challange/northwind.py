import sqlite3

# Connect to database and connect cursor
sl_conn = sqlite3.connect('northwind_small.sqlite3')
sl_curs = sl_conn.cursor()

# === Part 2 ===

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
print("\nAverage employee age: ", sl_curs.execute(sql_comm_4).fetchall())

# How does the average age of employee at hire vary by city?
sql_comm_5 = """
SELECT City, AVG(HireDate - BirthDate)
FROM Employee
GROUP BY City
"""
print("\nAverage employee age by city: ",
      sl_curs.execute(sql_comm_5).fetchall())



# === Part 3 ===

# What are the ten most expensive items (per unit price) in
# the database and their suppliers?
sql_comm_6 = """
SELECT ProductName, CompanyName, UnitPrice 
FROM Product
     INNER JOIN
     Supplier
     ON Product.SupplierID = Supplier.ID
ORDER BY UnitPrice DESC
Limit 10;
"""
print("\nTen most expensive items with supplier: ",
      sl_curs.execute(sql_comm_6).fetchall())

# What is the largest category (by number of unique products in it)?
sql_comm_7 = """
SELECT CategoryName, COUNT(DISTINCT Product.ID) AS CatSize
FROM Product
     INNER JOIN
     Category
     ON Product.CategoryID == Category.ID
GROUP BY CategoryID
ORDER BY CatSize DESC
LIMIT 1
"""
print("\nLargest category: ",
      sl_curs.execute(sql_comm_7).fetchall())

# Who's the employee with the most territories?
# Use TerritoryId (not name, region, or other fields)
# as the unique identifier for territories.
sql_comm_8 = """
SELECT FirstName, LastName, COUNT(DISTINCT TerritoryID) AS TerritoryNum
FROM Employee
     INNER JOIN
     EmployeeTerritory
     ON Employee.ID == EmployeeTerritory.EmployeeID
GROUP BY EmployeeID
ORDER BY TerritoryNum DESC
LIMIT 1
"""
print("\nEmployee with most terretories: ",
      sl_curs.execute(sql_comm_8).fetchall())

# Close cursor and connection
sl_curs.close()
sl_conn.close()
