s1 = str(input())
d = {}
for i in s1:
    if i not in d:
        d[i] = 0
    d[i] += 1
print(d)