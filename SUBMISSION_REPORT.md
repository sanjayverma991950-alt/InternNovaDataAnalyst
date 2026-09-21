# NOVA DATA ANALYTIC - PYTHON ASSIGNMENT REPORT (WEEK 1)

**Student Name:** Sanjay Kumar  
**Course:** Python for Data Analytics & AI  
**Assignment:** Week 1 Practical Tasks & Mini Project  
**Total Marks:** 100 / 100  

---

## Table of Contents

1. [Task 1: Python Basics](#task-1-python-basics)
2. [Task 2: Variables & Data Types](#task-2-variables--data-types)
3. [Task 3: Operators](#task-3-operators)
4. [Task 4: Conditional Statements](#task-4-conditional-statements)
5. [Task 5: Loops](#task-5-loops)
6. [Task 6: Functions](#task-6-functions)
7. [Task 7: Strings & Collections](#task-7-strings--collections)
8. [Task 8: Basic File Handling](#task-8-basic-file-handling)
9. [Task 9: Mini Python Project](#task-9-mini-python-project)
10. [Submission Guidelines & Drive Instructions](#submission-guidelines--drive-instructions)

---

## Task 1: Python Basics

### Objective
Create a program that prints a welcome banner, takes user details (Name, College Name, Branch) via keyboard input, and displays the information in a formatted profile card.

### Explanation
- Uses `input()` to prompt for student details from the console.
- Automatically provides sample default values if fields are left blank.
- Uses f-strings to format and display a clean student profile card.

### Source Code (`task1_basics.py`)
```python
# Task 1: Python Basics - Student Information Card

print("=" * 45)
print("           STUDENT INFORMATION")
print("=" * 45)

# Taking input from the user
name = input("Enter your Name: ")
college = input("Enter your College Name: ")
branch = input("Enter your Branch: ")

# If input is left blank, use default sample values
if not name:
    name = "Sanjay Kumar"
if not college:
    college = "Nova Institute of Technology"
if not branch:
    branch = "Computer Science & Data Analytics"

# Displaying the student card
print("\n" + "-" * 45)
print("               STUDENT CARD")
print("-" * 45)
print(f"Name         : {name}")
print(f"College Name : {college}")
print(f"Branch       : {branch}")
print("-" * 45)
```

### Sample Output
```text
=============================================
           STUDENT INFORMATION
=============================================
Enter your Name: Sanjay Kumar
Enter your College Name: Nova Institute of Technology
Enter your Branch: Computer Science & Data Analytics

---------------------------------------------
               STUDENT CARD
---------------------------------------------
Name         : Sanjay Kumar
College Name : Nova Institute of Technology
Branch       : Computer Science & Data Analytics
---------------------------------------------
```

---

## Task 2: Variables & Data Types

### Objective
Declare variables of four fundamental Python data types (Integer, Float, String, Boolean) and print each variable along with its runtime data type using `type()`.

### Explanation
- Demonstrates Python's dynamic typing across fundamental data types: string (`str`), integer (`int`), float (`float`), and boolean (`bool`).
- Inspects each variable's underlying data type using the built-in `type()` function in a clean, human-readable format.

### Source Code (`task2_variables.py`)
```python
# Task 2: Variables & Data Types

# Declaring variables of different data types
student_name = "Alex Johnson"   # String (str)
student_age = 21                # Integer (int)
student_gpa = 8.75              # Float (float)
is_enrolled = True              # Boolean (bool)

# Displaying each variable along with its data type
print("Student Name :", student_name, "--> Type:", type(student_name))
print("Student Age  :", student_age, "--> Type:", type(student_age))
print("Student GPA  :", student_gpa, "--> Type:", type(student_gpa))
print("Is Enrolled  :", is_enrolled, "--> Type:", type(is_enrolled))
```

### Sample Output
```text
Student Name : Alex Johnson --> Type: <class 'str'>
Student Age  : 21 --> Type: <class 'int'>
Student GPA  : 8.75 --> Type: <class 'float'>
Is Enrolled  : True --> Type: <class 'bool'>
```

---

## Task 3: Operators

### Objective
Create a calculator program that takes two numbers as input from the user and performs Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulus (`%`).

### Explanation
- Prompts for two numeric inputs converted with `float()`.
- Performs arithmetic calculations and formats the results cleanly.
- Checks that the divisor is non-zero before performing division or modulus to prevent zero division errors.

### Source Code (`task3_operators.py`)
```python
# Task 3: Operators - Simple Arithmetic Calculator

# Taking two numbers as input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Performing basic arithmetic operations
print("\n--- Arithmetic Operations ---")
print(f"Addition       : {num1} + {num2} = {num1 + num2}")
print(f"Subtraction    : {num1} - {num2} = {num1 - num2}")
print(f"Multiplication : {num1} * {num2} = {num1 * num2}")

# Handling division and modulus (checking for zero)
if num2 != 0:
    print(f"Division       : {num1} / {num2} = {num1 / num2:.2f}")
    print(f"Modulus        : {num1} % {num2} = {num1 % num2}")
else:
    print("Division and modulus cannot be performed with zero!")
```

### Sample Output
```text
Enter first number: 25
Enter second number: 4

--- Arithmetic Operations ---
Addition       : 25.0 + 4.0 = 29.0
Subtraction    : 25.0 - 4.0 = 21.0
Multiplication : 25.0 * 4.0 = 100.0
Division       : 25.0 / 4.0 = 6.25
Modulus        : 25.0 % 4.0 = 1.0
```

---

## Task 4: Conditional Statements

### Objective
Write a Python program that takes marks as input and displays the grade using `if`, `elif`, and `else` conditions according to the scheme:
- `90+` : Grade A
- `75–89` : Grade B
- `60–74` : Grade C
- `Below 60` : Fail

### Explanation
- Uses standard `if-elif-else` branches to determine grade cutoffs.
- Validates that entered marks fall within the valid range of 0 to 100.

### Source Code (`task4_conditionals.py`)
```python
# Task 4: Conditional Statements - Grade Calculator

# Taking marks as input
marks = float(input("Enter your marks (0 - 100): "))

# Evaluating grade based on marks
if marks < 0 or marks > 100:
    print("Invalid input! Marks should be between 0 and 100.")
elif marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

# Display result if input was valid
if 0 <= marks <= 100:
    print("\n--- Result ---")
    print(f"Marks : {marks}")
    print(f"Grade : {grade}")
```

### Sample Output
```text
Enter your marks (0 - 100): 82

--- Result ---
Marks : 82.0
Grade : B
```

---

## Task 5: Loops

### Objective
Write Python programs to:
1. Print numbers from 1 to 20 using a `for` loop.
2. Print the multiplication table of any number.
3. Print even numbers from 1 to 50 using a `while` loop.

### Explanation
- Uses `for i in range(1, 21)` to print numbers 1 through 20 on a single line.
- Generates a multiplication table from 1 to 10 for any user-inputted integer.
- Uses a `while` loop stepping by 2 to print even numbers between 1 and 50 efficiently.

### Source Code (`task5_loops.py`)
```python
# Task 5: Loops in Python (for and while)

# 1. Print numbers from 1 to 20 using a for loop
print("1. Numbers from 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print("\n")

# 2. Print multiplication table of a number using a for loop
num = int(input("Enter a number for multiplication table: "))
print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

# 3. Print even numbers between 1 and 50 using a while loop
print("3. Even numbers from 1 to 50:")
n = 2
while n <= 50:
    print(n, end=" ")
    n += 2
print()
```

### Sample Output
```text
1. Numbers from 1 to 20:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

Enter a number for multiplication table: 6

Multiplication Table of 6:
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60

3. Even numbers from 1 to 50:
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 
```

---

## Task 6: Functions

### Objective
Create two user-defined functions:
1. Function to calculate the square of a number.
2. Function to calculate the average of three numbers.
Call both functions with inputs provided by the user.

### Explanation
- Defines `calculate_square(num)` which returns `num ** 2`.
- Defines `calculate_average(a, b, c)` which returns `(a + b + c) / 3`.
- Calls both functions with user inputs and displays formatted outputs.

### Source Code (`task6_functions.py`)
```python
# Task 6: User-Defined Functions

# Function to calculate square of a number
def calculate_square(num):
    return num ** 2

# Function to calculate average of three numbers
def calculate_average(a, b, c):
    return (a + b + c) / 3


# 1. Calling calculate_square function
n = float(input("Enter a number to square: "))
print(f"Square of {n} is {calculate_square(n)}\n")

# 2. Calling calculate_average function
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

avg = calculate_average(n1, n2, n3)
print(f"Average of {n1}, {n2}, and {n3} is {avg:.2f}")
```

### Sample Output
```text
Enter a number to square: 7
Square of 7.0 is 49.0

Enter first number: 10
Enter second number: 20
Enter third number: 30
Average of 10.0, 20.0, and 30.0 is 20.00
```

---

## Task 7: Strings & Collections

### Objective
Demonstrate operations across Python's built-in data collections and string manipulation:
1. String operations: `upper()`, `lower()`, `replace()`, `find()`
2. List operations: `append()`, `remove()`, `sort()`
3. Tuple creation and indexing (positive and negative)
4. Dictionary storing student information
5. Set operations: `add()`, `remove()`, uniqueness, `union()`, `intersection()`

### Explanation
- Demonstrates case changes, text replacement, and substring index searching.
- Illustrates mutable list operations including adding, removing, and sorting elements in-place.
- Demonstrates immutable tuples with 0-based forward indexing and negative indexing.
- Stores key-value student data in a dictionary, iterates over items, and adds new keys.
- Shows set operations, automatic duplicate elimination, union, and intersection.

### Source Code (`task7_strings_collections.py`)
```python
# Task 7: Strings & Collections in Python

# 1. String Operations
print("--- 1. String Operations ---")
text = "Python Programming at Nova Data Analytics"
print("Original String :", text)
print("Uppercase       :", text.upper())
print("Lowercase       :", text.lower())
print("Replaced        :", text.replace("Nova Data Analytics", "Data Science Lab"))
print("Index of 'Nova' :", text.find("Nova"))
print()

# 2. List Operations
print("--- 2. List Operations ---")
courses = ["Python", "SQL", "Machine Learning", "Power BI"]
print("Initial list :", courses)

courses.append("Deep Learning")
print("After append :", courses)

courses.remove("SQL")
print("After remove :", courses)

courses.sort()
print("After sort   :", courses)
print()

# 3. Tuple & Indexing
print("--- 3. Tuple & Indexing ---")
student_tuple = ("Sanjay Kumar", 101, "Data Science", 2026)
print("Student Tuple        :", student_tuple)
print("First item [0]       :", student_tuple[0])
print("Second item [1]      :", student_tuple[1])
print("Last item [-1]       :", student_tuple[-1])
print("Second last item [-2]:", student_tuple[-2])
print()

# 4. Dictionary Operations
print("--- 4. Dictionary Operations ---")
student_dict = {
    "roll_no": 101,
    "name": "Sanjay Kumar",
    "branch": "Data Science",
    "marks": 92
}
print("Student Details:")
for key, value in student_dict.items():
    print(f"  {key}: {value}")

student_dict["grade"] = "A"
print("Updated Dictionary   :", student_dict)
print()

# 5. Set Operations
print("--- 5. Set Operations ---")
skills = {"Python", "SQL", "Tableau"}
print("Initial set          :", skills)

skills.add("Pandas")
skills.add("Python")  # Adding duplicate (ignored by set)
print("After adding 'Pandas' & duplicate 'Python':", skills)

skills.remove("Tableau")
print("After removing 'Tableau':", skills)

extra_skills = {"Python", "NumPy", "Git"}
print("Second set           :", extra_skills)
print("Union                :", skills.union(extra_skills))
print("Intersection         :", skills.intersection(extra_skills))
```

### Sample Output
```text
--- 1. String Operations ---
Original String : Python Programming at Nova Data Analytics
Uppercase       : PYTHON PROGRAMMING AT NOVA DATA ANALYTICS
Lowercase       : python programming at nova data analytics
Replaced        : Python Programming at Data Science Lab
Index of 'Nova' : 22

--- 2. List Operations ---
Initial list : ['Python', 'SQL', 'Machine Learning', 'Power BI']
After append : ['Python', 'SQL', 'Machine Learning', 'Power BI', 'Deep Learning']
After remove : ['Python', 'Machine Learning', 'Power BI', 'Deep Learning']
After sort   : ['Deep Learning', 'Machine Learning', 'Power BI', 'Python']

--- 3. Tuple & Indexing ---
Student Tuple        : ('Sanjay Kumar', 101, 'Data Science', 2026)
First item [0]       : Sanjay Kumar
Second item [1]      : 101
Last item [-1]       : 2026
Second last item [-2]: Data Science

--- 4. Dictionary Operations ---
Student Details:
  roll_no: 101
  name: Sanjay Kumar
  branch: Data Science
  marks: 92
Updated Dictionary   : {'roll_no': 101, 'name': 'Sanjay Kumar', 'branch': 'Data Science', 'marks': 92, 'grade': 'A'}

--- 5. Set Operations ---
Initial set          : {'Tableau', 'Python', 'SQL'}
After adding 'Pandas' & duplicate 'Python': {'Tableau', 'Python', 'SQL', 'Pandas'}
After removing 'Tableau': {'Python', 'SQL', 'Pandas'}
Second set           : {'NumPy', 'Python', 'Git'}
Union                : {'Python', 'Git', 'SQL', 'NumPy', 'Pandas'}
Intersection         : {'Python'}
```

---

## Task 8: Basic File Handling

### Objective
Write a Python program that creates a text file, writes an introduction profile into the file, and reads and displays the file contents on the console.

### Explanation
- Uses Python's standard `with open(..., "w")` block to write student profile information safely into `student_introduction.txt`.
- Uses `with open(..., "r")` to read the entire file content and print it directly to the console.

### Source Code (`task8_file_handling.py`)
```python
# Task 8: Basic File Handling (Writing and Reading a Text File)

filename = "student_introduction.txt"

# 1. Writing profile information to the file
print("--- Enter Profile Information ---")
name = input("Enter your name: ") or "Sanjay Kumar"
college = input("Enter your college: ") or "Nova Institute of Technology"
branch = input("Enter your branch: ") or "Computer Science & Data Analytics"
bio = input("Enter a short bio: ") or "Aspiring Data Analyst passionate about Python and AI."

with open(filename, "w") as f:
    f.write("============================================================\n")
    f.write("                STUDENT INTRODUCTION PROFILE                \n")
    f.write("============================================================\n")
    f.write(f"Full Name       : {name}\n")
    f.write(f"College / Univ  : {college}\n")
    f.write(f"Branch / Stream : {branch}\n")
    f.write(f"About Me        : {bio}\n")
    f.write("Course Enrolled : Python for Data Analytics & AI\n")
    f.write("Status          : Active Learner - Nova Data Analytic Week 1\n")
    f.write("============================================================\n")

print(f"\nProfile successfully saved to '{filename}'.\n")

# 2. Reading and displaying file contents
print("--- Reading File Content ---")
with open(filename, "r") as f:
    content = f.read()
    print(content)
```

### Sample Output
```text
--- Enter Profile Information ---
Enter your name: Sanjay Kumar
Enter your college: Nova Institute of Technology
Enter your branch: Computer Science & Data Analytics
Enter a short bio: Aspiring Data Analyst passionate about Python and AI.

Profile successfully saved to 'student_introduction.txt'.

--- Reading File Content ---
============================================================
                STUDENT INTRODUCTION PROFILE                
============================================================
Full Name       : Sanjay Kumar
College / Univ  : Nova Institute of Technology
Branch / Stream : Computer Science & Data Analytics
About Me        : Aspiring Data Analyst passionate about Python and AI.
Course Enrolled : Python for Data Analytics & AI
Status          : Active Learner - Nova Data Analytic Week 1
============================================================
```

---

## Task 9: Mini Python Project

### Project Title: Student Record Management System
A clean console application providing full record management (Add, Display, Search, Delete, Grade calculation, and Exit).

### Key Features
1. **Add Student Record:** Collects Roll Number, Name, Branch, and Marks with duplicate roll number checks and validation.
2. **Display All Records:** Prints all student records in a clean table layout.
3. **Search Student by Name:** Performs case-insensitive matching across registered students.
4. **Delete Student Record:** Removes a record by Roll Number using Python's standard `.remove()`.
5. **Automatic Grade Calculation:** Assigns grade (`A`, `B`, `C`, `Fail`) from marks.

### Source Code (`task9_student_management.py`)
```python
# Task 9: Mini Project - Student Record Management System

# Pre-populated list of student records for demonstration
students = [
    {"roll_no": "101", "name": "Aarav Mehta", "branch": "Computer Science", "marks": 94.0, "grade": "A"},
    {"roll_no": "102", "name": "Sneha Sharma", "branch": "Data Analytics", "marks": 82.5, "grade": "B"},
    {"roll_no": "103", "name": "Vikram Rao", "branch": "Information Tech", "marks": 67.0, "grade": "C"}
]

def calculate_grade(marks):
    """Returns letter grade based on marks."""
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"

def add_student():
    """Adds a new student record."""
    print("\n--- Add New Student ---")
    roll_no = input("Enter Roll Number: ")

    # Check if roll number already exists
    for s in students:
        if s["roll_no"] == roll_no:
            print(f"Error: Roll number '{roll_no}' already exists.")
            return

    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = float(input("Enter Marks (0 - 100): "))

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        return

    grade = calculate_grade(marks)

    student = {
        "roll_no": roll_no,
        "name": name,
        "branch": branch,
        "marks": marks,
        "grade": grade
    }
    students.append(student)
    print(f"Student '{name}' added successfully!")

def display_all():
    """Displays all student records in a table format."""
    print("\n--- Student Records ---")
    if not students:
        print("No student records found.")
        return

    print(f"{'Roll No':<10} {'Name':<20} {'Branch':<20} {'Marks':<8} {'Grade':<6}")
    print("-" * 68)
    for s in students:
        print(f"{s['roll_no']:<10} {s['name']:<20} {s['branch']:<20} {s['marks']:<8.2f} {s['grade']:<6}")
    print("-" * 68)
    print(f"Total Students: {len(students)}")

def search_student():
    """Searches for a student by name."""
    print("\n--- Search Student ---")
    search_name = input("Enter student name to search: ")

    found = False
    for s in students:
        if search_name.lower() in s["name"].lower():
            if not found:
                print("\nMatch Found:")
                print(f"{'Roll No':<10} {'Name':<20} {'Branch':<20} {'Marks':<8} {'Grade':<6}")
                print("-" * 68)
                found = True
            print(f"{s['roll_no']:<10} {s['name']:<20} {s['branch']:<20} {s['marks']:<8.2f} {s['grade']:<6}")

    if not found:
        print(f"No student found with name matching '{search_name}'.")
    else:
        print("-" * 68)

def delete_student():
    """Deletes a student record by roll number."""
    print("\n--- Delete Student ---")
    roll_no = input("Enter Roll Number to delete: ")

    for s in students:
        if s["roll_no"] == roll_no:
            students.remove(s)
            print(f"Student '{s['name']}' (Roll No: {roll_no}) deleted successfully!")
            return

    print(f"Student with Roll Number '{roll_no}' not found.")

# Main menu loop
while True:
    print("\n=== Student Record Management System ===")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting application. Goodbye!")
        break
    else:
        print("Invalid choice! Please choose between 1 and 5.")
```

### Sample Output
```text
=== Student Record Management System ===
1. Add Student
2. Display All Students
3. Search Student by Name
4. Delete Student
5. Exit
Enter your choice (1-5): 2

--- Student Records ---
Roll No    Name                 Branch               Marks    Grade 
--------------------------------------------------------------------
101        Aarav Mehta          Computer Science     94.00    A     
102        Sneha Sharma         Data Analytics       82.50    B     
103        Vikram Rao           Information Tech     67.00    C     
--------------------------------------------------------------------
Total Students: 3

=== Student Record Management System ===
1. Add Student
2. Display All Students
3. Search Student by Name
4. Delete Student
5. Exit
Enter your choice (1-5): 1

--- Add New Student ---
Enter Roll Number: 104
Enter Name: Priya Patel
Enter Branch: AI & Robotics
Enter Marks (0 - 100): 91
Student 'Priya Patel' added successfully!

=== Student Record Management System ===
1. Add Student
2. Display All Students
3. Search Student by Name
4. Delete Student
5. Exit
Enter your choice (1-5): 3

--- Search Student ---
Enter student name to search: Priya

Match Found:
Roll No    Name                 Branch               Marks    Grade 
--------------------------------------------------------------------
104        Priya Patel          AI & Robotics        91.00    A     
--------------------------------------------------------------------

=== Student Record Management System ===
1. Add Student
2. Display All Students
3. Search Student by Name
4. Delete Student
5. Exit
Enter your choice (1-5): 4

--- Delete Student ---
Enter Roll Number to delete: 103
Student 'Vikram Rao' (Roll No: 103) deleted successfully!

=== Student Record Management System ===
1. Add Student
2. Display All Students
3. Search Student by Name
4. Delete Student
5. Exit
Enter your choice (1-5): 5
Exiting application. Goodbye!
```

---

## Submission Guidelines & Drive Instructions

### Preparing the PDF Submission
1. Open this report (`SUBMISSION_REPORT.md`) in VS Code or any Markdown viewer/browser.
2. In VS Code: Press `Ctrl + Shift + P` -> choose **Markdown PDF: Export (pdf)**, OR right-click -> **Print** -> Save as PDF.
3. You can paste actual terminal screenshots directly below each task's section in the PDF if preferred.

### Google Drive Upload
1. Open your Google Drive: `https://drive.google.com`.
2. Click **New** -> **Folder upload** (or create a folder named `NovaDataAnalytic_Week1_Python`).
3. Select the workspace directory:
   `c:\Users\sanjay\OneDrive\Pictures\OneDrive\Desktop\NovaDataAnalytic`
4. Ensure the folder contains:
   - `task1_basics.py`
   - `task2_variables.py`
   - `task3_operators.py`
   - `task4_conditionals.py`
   - `task5_loops.py`
   - `task6_functions.py`
   - `task7_strings_collections.py`
   - `task8_file_handling.py`
   - `task9_student_management.py`
   - `student_introduction.txt`
   - `SUBMISSION_REPORT.md`
5. Right click the uploaded Google Drive folder -> Click **Share** -> Change general access to **"Anyone with the link can view"** -> Copy link.
6. Paste the Google Drive link into your final submission along with your name and college details.
