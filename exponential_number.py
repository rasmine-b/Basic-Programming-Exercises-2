# Create a program that ask use to input 2 numbers. Print the remainder when the first number is divided by the second number

while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        remainder = num1 % num2
        print(f"The remainder of 2 numbers is {remainder}")
        break
    except ValueError:
        print("Error.")