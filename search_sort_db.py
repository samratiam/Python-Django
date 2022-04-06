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


# execute query
cur.execute("SELECT id,name,age FROM student")

# fetch all rows from the table
rows = cur.fetchall()


# Convert each rows data tuple to list
rows_list = []
for r in rows:
    rows_list.append(list(r))
print("----------------")
print("Rows in List:", rows_list)
print("----------------")

# Sort the data according to their age
for i in range(1, len(rows_list)):
    key = rows_list[i][2]
    j = i-1
    while j >= 0 and key < rows_list[j][2]:
        rows_list[j+1][2] = rows_list[j][2]
        j -= 1
    rows_list[j+1][2] = key

print("Sorted data on the basis of age:", rows_list)
print("----------------")

# Binary Search

# First Sort the names of student
for i in range(1, len(rows_list)):
    key = rows_list[i][1]
    j = i-1
    while j >= 0 and key < rows_list[j][1]:
        rows_list[j+1][1] = rows_list[j][1]
        j -= 1
    rows_list[j+1][1] = key

print("Sorted data on the basis of name:", rows_list)
print("----------------")

# Implement binary


def binary_search(i, j, key, rows_list):
    if i <= j:
        mid = (i + j) // 2
        if key == rows_list[mid][1]:
            print(f"{key} is found on the row no. {mid+1} of database")
            print("----------------")
            print(f"Show entries of {key}")

            print(
                f"ID: {rows_list[mid][0]} Name:{rows_list[mid][1]} Age:{rows_list[mid][2]}")
        elif key > rows_list[mid][1]:
            i = mid + 1
            return binary_search(i, j, key, rows_list)

        elif key < rows_list[mid][1]:
            j = mid - 1
            return binary_search(i, j, key, rows_list)
    else:
        print(f"{key} isn't found in the database")


key = input("Enter the student name you want to find:")
# key = 'Samrat Pudasaini'
binary_search(0, len(rows_list), key, rows_list)

# commit the changes to insert the data
con.commit()

# close the cursor
cur.close()

# close the connection
con.close()
