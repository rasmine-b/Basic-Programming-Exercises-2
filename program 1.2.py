# Create a program that ask user to input 2 numbers. Print the smaller number.

while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))

        if num1 < num2:
            print(f"The smaller number is {num1:.0f}")
        elif num2 < num1:
            print(f"The smaller number is {num2:.0f}")
        else:
            print("Enter a smaller number.")
        break
    except ValueError:
        print("Error.")