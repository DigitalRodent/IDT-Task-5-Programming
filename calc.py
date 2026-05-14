num1 = 0
num2 = 0

print("This program is for calculating two numbers.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} x {num2} = {multiplication}")
if num2 != 0:
    division = num1 / num2
    print(f"{num1} / {num2} = {division}")
else:
    print("You cannot divide by zero.")
print("\n")
input("Press Enter to exit.")