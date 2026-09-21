print("Numbers from 1 to 20:")

for number in range(1, 21):
    print(number)


number = int(input("Enter a number: "))

print(f"\nMultiplication Table of {number}")

for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")


number = 2

print("Even numbers from 1 to 50:")

while number <= 50:
    print(number)
    number += 2
