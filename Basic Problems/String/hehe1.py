#Input in a list
result = ''
a=list()
n=int(input("enter the no of elements: "))
for i in range(int(n)):
   k=int(input("Enter elements: "))
   a.append(k)
evenlist = []
oddlist = []
for i in a:
    if i % 2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)
result = ' '.join([str(i) for i in evenlist+oddlist])
print(result)