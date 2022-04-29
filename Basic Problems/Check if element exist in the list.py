a = int(input("Check if number exists in the list "))
MyList = [1,2,3,4,5,6,7]
for i in MyList:
    if i == a:
        print(i,"Exists in the list")
        break
else:
    print(a,"Doesn't Exist in the list")
        