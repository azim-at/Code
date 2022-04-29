def splitevenodd(A): 
   evenlist = [] 
   oddlist = [] 
   result = ''
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i) 
      else: 
         oddlist.append(i) 
   result = ' '.join([str(i) for i in evenlist+oddlist])
   print(result)

A=list()
n=int(input())
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
splitevenodd(A) 