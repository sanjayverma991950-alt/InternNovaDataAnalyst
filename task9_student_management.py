students = []


def add_student():
    name = input("Enter student name: ").strip()
    age = int(input("Enter student age: "))
    branch = input("Enter student branch: ").strip()
    marks = float(input("Enter student marks: "))

    student = {
        "name": name,
        "age": age,
        "branch": branch,
        "marks": marks
    }

    students.append(student)
    print("\nStudent added successfully.")


def display_students():
    if not students:
        print("\nNo student records found.")
        return

    print("\n" + "=" * 50)
    print("             STUDENT RECORDS")
    print("=" * 50)

    for student in students:
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Branch : {student['branch']}")
        print(f"Marks  : {student['marks']}")
        print("-" * 50)


def search_student():
    name = input("Enter the student name to search: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found")
            print("-" * 30)
            print("Name   :", student["name"])
            print("Age    :", student["age"])
            print("Branch :", student["branch"])
            print("Marks  :", student["marks"])
            return

    print("\nStudent not found.")


def delete_student():
    name = input("Enter the student name to delete: ").strip()

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("\nStudent deleted successfully.")
            return

    print("\nStudent not found.")


while True:
    print("\n" + "=" * 40)
    print("     STUDENT RECORD MANAGEMENT")
    print("=" * 40)
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using the Student Record System.")
        break

    else:
        print("Invalid choice. Please try again.")
