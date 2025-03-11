# Create a program that ask user to input 2 numbers. Print the quotient of the 2 numbers without the decimal point

while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        num_quotient = num1 / num2
        print(f"The quotient of the 2 numbers is {num_quotient:.0f}")
        break
    except ValueError:
        print("Error.")