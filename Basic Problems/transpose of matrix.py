x= [[1,2,3],
    [4,5,6],
    [7,8,9]]

row = [[x[j][i] for j in range(len(x[0]))]
       for i in range(len(x))]
for k in row:
    print(k)