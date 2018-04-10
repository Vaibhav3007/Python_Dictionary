my_str = "At age six when Hathaway watched her mother perform in Les Misérables as Fantine she instantly became fascinated with the stage but her parents were not keen on allowing her to pursue an acting career"
print(my_str)
my_str_low = my_str.lower()
my_list = my_str_low.split()
my_list.sort()

my_dict = {}

for i in my_list:
    if i[0] not in my_dict:
        my_dict[i[0]] = []
        my_dict[i[0]].append(i)
    else:
        my_dict[i[0]].append(i)

for k,v in my_dict.items():
    print(k,":",v)
