import psycopg2

# connect to the db
con = psycopg2.connect(
    host="localhost",
    database="college",
    user="postgres",
    password="samrat"
)

# cursor
cur = con.cursor()

cur.execute(
    "CREATE TABLE student (id INTEGER PRIMARY KEY, name VARCHAR(100), age INTEGER) "
)

# insert the values into database
cur.execute("INSERT INTO student VALUES (%s, %s, %s)",
            (1, "Ayush Baral", 26))
cur.execute("INSERT INTO student VALUES (%s, %s, %s)",
            (2, "Samrat Pudasaini", 24))


# execute query
cur.execute("SELECT id,name,age FROM student")

# fetch all rows from the table
rows = cur.fetchall()

for r in rows:
    print(f"id: {r[0]} name: {r[1]} age: {r[2]}")

# commit the changes to insert the data
con.commit()

# close the cursor
cur.close()

# close the connection
con.close()
