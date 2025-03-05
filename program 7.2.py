# Create a program that ask user to input 10 numbers. Print how many are even numbers.

num_list = []
while True:
    try:
        for i in range (1,11):
            num = float(input(f"Enter a number{i}: "))
            if num % 2 == 0:
                num_list.append(num)
        print(f"The number of even numbers is {len(num_list)}")
        break
    except ValueError:
        print("Error.")

