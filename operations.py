from student import Student
from database import connect_db


def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    student = Student(roll, name, marks)

    conn, cursor = connect_db()

    try:
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?)",
            (student.roll, student.name, student.marks)
        )

        conn.commit()

        print("Student Added Successfully!")

    except:
        print("Roll Number already exists.")

    conn.close()


def view_students():
    conn, cursor = connect_db()

    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    if len(data) == 0:
        print("No student records found.")

    else:
        print("\nStudent Records")

        for student in data:
            print(f"Roll: {student[0]}, Name: {student[1]}, Marks: {student[2]}")

    conn.close()


def search_student():
    roll_number = input("Enter Roll Number to Search: ")

    conn, cursor = connect_db()

    cursor.execute(
        "SELECT * FROM students WHERE roll = ?",
        (roll_number,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print(f"Roll: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Marks: {student[2]}")

    else:
        print("Student not found.")

    conn.close()
