# Python Program to demonstrate working of array(),append(),insert()
import array

#Initailizing Array()
arr = array.array('i',[1,2,3,4])

print("Array created is:",end=" ")
for i in range(0,4):
    print(arr[i],end=" ")

print("\r")

#Using Append()
arr.append(5)
print("Appended array is:",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")

print("\r")

#Using Insert()
arr.insert(4,1)
print("Inserted element is:",end=" ")
for i in range(0,6):
    print(arr[i],end=" ")

print("\r")

#Using Pop()
arr.pop(3)
print("Poped element is:",end=" ")
for i in range(0,5):
    print(arr[i],end=" ")

print("\r")

#Using Remove()
arr.remove(1)
print("Removed value from array is:",end=" ")
for i in range(0,4):
    print(arr[i],end=" ")

print("\r")

#using Index()
arr.index(3)
print("Index value is:",arr[i],end=" ")

print("\r")

#Using Reverse()
arr.reverse()
print("Reversed array is:",end=" ")
for i in range(0,4):
    print(arr[i],end=" ")
    
    