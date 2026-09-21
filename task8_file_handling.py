introduction = """
My name is Sanjay Kumar.
I am a student of Nova Institute of Technology.
My branch is Computer Science & Data Analytics.
I am currently learning Python for Data Analytics.
"""

with open("introduction.txt", "w") as file:
    file.write(introduction)

with open("introduction.txt", "r") as file:
    content = file.read()

print("File Contents:")
print("-" * 30)
print(content)
