dict1 = {1:1,2:4,3:9,4:16,5:25}
print(dict1)
for i in [0,3,2,7,16]:
    if i in dict1.keys():
        print(i,"is in dict keys")
    else:
        print(i,"is not in dict keys")
