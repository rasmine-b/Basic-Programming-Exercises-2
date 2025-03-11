# Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five

num_list = []

for i in range (0,101):
    if i % 10 != 0 and i % 10 != 5:
        num_list.append(i)
print(num_list)
    
