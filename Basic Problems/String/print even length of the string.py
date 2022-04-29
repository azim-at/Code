a = "This is a python language"
lis = a.split()
print(lis)
for x in lis:
    if len(x)%2==0:
        print(x)