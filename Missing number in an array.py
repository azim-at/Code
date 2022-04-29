myArray = [1,2,3,4,5,6,7,8,9,10]
n = [1,3,5,6,7,9]
res = list()
for i in myArray:
    if i != n:
        res.append(i)
print(res)