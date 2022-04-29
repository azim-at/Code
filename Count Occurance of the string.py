string = "azim s azim azim".split()
subString = str(input())
counter = 0
for x in string:
    if x == subString:
        counter += 1
print(counter)