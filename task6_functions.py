def square(number):
    return number * number


def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3


number = float(input("Enter a number to find its square: "))
print("Square:", square(number))

print("\nEnter three numbers to calculate their average:")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))
num3 = float(input("Third number: "))

print("Average:", average(num1, num2, num3))
