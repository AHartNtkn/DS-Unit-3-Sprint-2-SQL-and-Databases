import sqlite3

# Create new database and connect cursor
sl_conn = sqlite3.connect('demo_data.sqlite3')
sl_curs = sl_conn.cursor()

# Create table with correct types and names
create_demo_table = """
CREATE TABLE demo_table (
    id SERIAL PRIMARY KEY,
    s varchar(1),
    x INT,
    y INT
);
"""
sl_curs.execute(create_demo_table)

# Populate table
demo_insert = """
INSERT INTO demo_table
(s, x, y)
VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);
"""
sl_curs.execute(demo_insert)

# Close cursor and commit chances
sl_curs.close()
sl_conn.commit()

# Create fresh cursor
sl_curs = sl_conn.cursor()

# Count how many rows you have - it should be 3!
sql_comm_1 = "SELECT COUNT(*) FROM demo_table;"
print("Rows: ", sl_curs.execute(sql_comm_1).fetchall())

"""
Rows:  [(3,)]
"""

# How many rows are there where both x and y are at least 5?
sql_comm_2 = """
SELECT COUNT(*)
FROM demo_table
WHERE x >= 5
  AND y >= 5;
"""
print("where both x and y are at least 5: ",
      sl_curs.execute(sql_comm_2).fetchall())

"""
where both x and y are at least 5:  [(2,)]
"""

# How many unique values of y are there
sql_comm_2 = """
SELECT COUNT(DISTINCT y)
FROM demo_table
"""
print("Distinct y values: ",
      sl_curs.execute(sql_comm_2).fetchall())

"""
Distinct y values:  [(2,)]
"""

# Close cursor and connection
sl_curs.close()
sl_conn.close()
