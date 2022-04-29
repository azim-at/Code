s1= str(input())
s2 = "geeks for geeks"

lis = s2.split()

for i in lis:
    if i == s1:
        print(s1, "is present in the",s2)
        break
    else:
        print(s1, "is not present in the",s2)
        break
        