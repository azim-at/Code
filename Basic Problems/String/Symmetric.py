s = input("Enter the String:")
a = len(s)

flag = 1

if a%2:
    mid = a//2+1
else:
    mid = a//2

start1 = 0
start2 = mid

while start1 < mid and start2 < a:
    if s[start1] == s[start2]:
        start1 = start1 + 1
        start2 = start2 + 1
    else:
        flag = 0
        break
if flag == 1:
    print("String is Symmetric")
else:
    print("String is not Symmetric")
    