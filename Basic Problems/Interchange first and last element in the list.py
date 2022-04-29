def Swap(MyList):
    size = len(MyList)

    temp = MyList[0]
    MyList[0] = MyList[size-1]
    MyList[size-1] = temp

    return MyList
MyList = [1,2,3,4,5]
print(Swap(MyList))