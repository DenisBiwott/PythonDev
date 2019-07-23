import psycopg2

# psycopg2 is a PostgreSQL database adapter for the Python programming language(pip install psycopg2)
c = psycopg2.connect(  # to create a connection instance to the specified database
    host="localhost",
    port=5432,
    user="school_user",
    password="school_password",
    dbname="testdatabasse"

)

# bound to the connection for the session's entire lifetime is the cursor() object
#  Allows Python code to execute PostgreSQL command in a database session.
cur = c.cursor()

# To create a table called company
# the execute() method executes SQL queries
cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')

# To create a table called audit
# the execute() method executes SQL queries
cur.execute('''CREATE TABLE AUDIT
      (EMP_ID INT NOT NULL,
       ENTRY_DATE TEXT NOT NULL);''')
print("Table created successfully")

# c.close()   # closes the database connection

# To insert data into the table
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")


print("Inserted successfully")


query = 'SELECT * FROM COMPANY'
cur.execute(query)
for row in cur.fetchall():  # fetchall() fetches all rows of a query result
    print(row)
c.commit()
