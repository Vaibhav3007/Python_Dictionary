num = [x for x in range(1,11)]
cube = [y**3 for y in range(1,11)]

cube_dict = {}

for i in range(len(num)):
    cube_dict[num[i]] = cube[i]

print("List 1 ",num,type(num))
print("List 2 ",cube,type(cube))
print("Dictionary ",cube_dict,type(cube_dict))
