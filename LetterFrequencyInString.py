my_string = "Stack Overflow is a community of 8.5 million programmers, just like you, helping each other."
test = "ssupperrr aadbrr"

print(my_string)
my_dict = {}

for i in my_string:
    freq = my_string.count(i)
    if i not in my_dict:
        my_dict[i] = freq
print(my_dict)
