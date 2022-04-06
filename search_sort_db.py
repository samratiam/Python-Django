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


def binary_search(i, j, key, array):
    if i <= j:
        mid = (i + j) // 2
        if key == array[mid]:
            for r in rows:
                if key == r[1]:
                    print(f"{key} is found on the database")
                    print("Show the entries:")
                    print(f"id: {r[0]} name: {r[1]} age: {r[2]}")
                    break

        elif key > array[mid]:
            i = mid + 1
            return binary_search(i, j, key, array)

        elif key < array[mid]:
            j = mid - 1
            return binary_search(i, j, key, array)

    else:
        print(f"{key} isn't found in the database")


# key = str(input("Enter the student name you want to find:"))


# commit the changes to insert the data
con.commit()

# close the cursor
cur.close()

# close the connection
con.close()
