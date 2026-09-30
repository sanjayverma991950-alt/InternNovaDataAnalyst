# Task 7: Strings and Collections

# String Operations

text = "Python Programming"

print("\nString Operations")
print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("Python", "Data"))
print("Position:", text.find("Programming"))


# List Operations

numbers = [40, 10, 30, 20]

print("\nList Operations")
print("Original list:", numbers)

numbers.append(50)
print("After append:", numbers)

numbers.remove(10)
print("After remove:", numbers)

numbers.sort()
print("After sort:", numbers)


# Tuple Creation and Indexing

student = ("Sanjay", 21, "Computer Science")

print("\nTuple Operations")
print("Tuple:", student)
print("Name:", student[0])
print("Age:", student[1])
print("Branch:", student[2])


# Dictionary Operations

student = {
    "name": "Sanjay Kumar",
    "age": 21,
    "college": "Nova Institute of Technology",
    "branch": "Computer Science & Data Analytics"
}

print("\nDictionary Operations")
print("Name:", student["name"])
print("Age:", student["age"])
print("College:", student["college"])
print("Branch:", student["branch"])


# Set Operations

numbers = {10, 20, 30, 40}

print("\nSet Operations")
print("Original set:", numbers)

numbers.add(50)
print("After add:", numbers)

numbers.remove(20)
print("After remove:", numbers)
