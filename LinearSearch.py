#Linear Search Program
lis = [1,2,3,4,1,23,4,34,5,22,2,1,3,4,9,8,7]
print("Enter the element to be searched:")
n = int(input())
flag = 0
for index,data in enumerate(lis):
    if data == n:
        flag = 1
        print("The Element",data,"is present at the index",index)
if flag == 0:
    print("Element is not present")