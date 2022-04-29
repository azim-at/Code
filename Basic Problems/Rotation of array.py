def leftarray(arr,n,d):
    for i in range(d):
        leftarraybyOne(arr,n)

def leftarraybyOne(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def PrintArray(arr,n):
    for i in range(0,n):
        print(arr[i],end=" ")

arr = [1,2,3,4,5,6,7]
leftarray(arr, 7, 2)
PrintArray(arr, 7)
        
     

        
    