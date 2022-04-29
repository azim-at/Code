x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[9,8,7],
     [6,5,4],
     [3,2,1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

result1 = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
        result1[i][j] = x[i][j] - y[i][j]
for i in result:
    print(i)
for i in result1:
    print(i)
            
            
            
        
    
    
     

