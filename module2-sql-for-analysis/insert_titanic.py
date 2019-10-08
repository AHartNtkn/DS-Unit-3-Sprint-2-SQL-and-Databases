import psycopg2
import pandas as pd

dbname = "izwhyriw"
user = "izwhyriw"
password = "OsPabQ1kWOH-F3ONCaxsoXcV6h9kwJim"
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname,
                           user = user,
                           password = password,
                           host = host)

pg_curs = pg_conn.cursor()

titanic_df = pd.read_csv('titanic.csv')

create_titanic_table = """
CREATE TABLE titanic (
    index SERIAL PRIMARY KEY,
    Survived INT,
    Pclass INT,
    Name varchar(100),
    Sex varchar(6),
    Age FLOAT,
    "Siblings/Spouses Aboard" INT,
    "Parents/Children Aboard" INT,
    Fare FLOAT
); 
"""

pg_curs.execute(create_titanic_table)

all_values = ", ".join(["("+ str(c[0]) +
                        ", "+ str(c[1]) +
                        ", \'"+ str(c[2]).replace("\'","`") +
                        "\', \'"+ str(c[3]) +
                        "\', "+ str(c[4]) +
                        ", "+ str(c[5]) +
                        ", "+ str(c[6]) +
                        ", "+ str(c[7]) +
                        ")" for c in list(titanic_df.values)])

insert_all = """
INSERT INTO titanic
(Survived, Pclass, Name, Sex, Age, \"Siblings/Spouses Aboard\",
 \"Parents/Children Aboard\", Fare)
VALUES """ + all_values + ";"

pg_curs.execute(insert_all)

pg_curs.close()

pg_conn.commit()

pg_conn.close()