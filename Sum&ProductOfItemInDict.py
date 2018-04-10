#Programatic dictionary generation

my_dict = {x:x**x for x in range(1,6)}

print(my_dict)

c = 1
d = 1
keys = list(my_dict.keys())
values = list(my_dict.values())

for i in range(len(keys)):
    c = c*keys[i]
    d = d*values[i]

print("Product of keys- ",c)
print("Product of values- ",d)
print("Sum of keys- ",sum(keys))
print("Sum of values- ",sum(values))
