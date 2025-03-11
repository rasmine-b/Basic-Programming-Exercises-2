# Create a program that ask user to input 10 numbers. Print print the result of the first number minus all of the remaining numbers

num_list = []
while True:
    try:
        for i in range (1,11):
            num = float(input(f"Enter a number{i}: "))
            num_list.append(num)
        
        result = num_list[0]

        for num in num_list [1:]:
            result -= num
        print(f"The difference of the first number and the remaining numbers is {result}")
        break
    
    except ValueError:
        print("Error.")
