#remove i'th character from the string
words = "i like programming so much"
aa = ""
for i in range(len(words)):
    if i != 4:
        aa = aa + words[i]
print(aa)
