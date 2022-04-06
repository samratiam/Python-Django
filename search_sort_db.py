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

#print("Rows:", rows)

# Sort the list of ages


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


age_list = []  # List of ages
student_list = []  # List of students names

# Traversing through each row of the student table
print("Student Table Data:")
for r in rows:
    print(f"id: {r[0]} name: {r[1]} age: {r[2]}")
    age_list.append(r[2])
    student_list.append(r[1])

# Sort the ages
insertionSort(age_list)
print("Sorted Ages:", age_list)

# Sort the student names
insertionSort(student_list)
print("Sorted Student names:", student_list)

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


key = str(input("Enter the student name you want to find:"))
binary_search(0, len(student_list)-1, key, student_list)

# commit the changes to insert the data
con.commit()

# close the cursor
cur.close()

# close the connection
con.close()
