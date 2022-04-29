vowels = set("aeiouAEIOU")
n = str(input("Enter to check the vowels: "))
store = set()
for i in vowels:
    if i in n:
        store.add(i)
    else:
        pass
if vowels == store:
    print("Accepted")
else:
    print("Not Accepted")