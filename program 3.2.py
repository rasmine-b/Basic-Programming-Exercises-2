# Create a program that ask user to input 2 numbers. Print the difference of the two numbers

while True:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        diff_num = num1 - num2
        print(f"The difference of the 2 numbers is {diff_num:.2f}")
        break
    except ValueError:
        print("Error.")