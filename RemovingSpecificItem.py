my_dict = {x:x**2 for x in range(1,11)}

print(my_dict)

n = int(input("Enter the key to remove "))

my_dict.pop(n)

print(my_dict)
