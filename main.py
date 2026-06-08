from database import conn, cursor

while True:

    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?)",
            (roll, name, marks)
        )

        conn.commit()

        print("Student Added Successfully!")

    elif choice == "2":

        cursor.execute("SELECT * FROM students")

        data = cursor.fetchall()

        print("\nStudent Records")

        for student in data:
            print(student)

    elif choice == "3":

        roll = input("Enter Roll Number to Search: ")

        cursor.execute(
            "SELECT * FROM students WHERE roll = ?",
            (roll,)
        )

        student = cursor.fetchone()

        if student:
            print(student)

        else:
            print("Student Not Found")

    elif choice == "4":
        break

    else:
        print("Invalid Choice")
