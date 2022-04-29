arr = [12,11,7,8,9,10]
n = len(arr)
for i in range(0, 2): 
    a = arr[0]
    for j in range(0, n-1):
        arr[j] = arr[j + 1]
          
    arr[n-1] = a
for i in range(0,n):
    print(arr[i])
    

    