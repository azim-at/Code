#find the length of the string using 'for' loop
string = str(input("Enter the string to check the length:" ))
new = ""
counter = 0
for i in string:
    new = i
    if i == new:
        counter += 1
print("The Length of the given is:",counter) #prints the length

#using len()
print("The Length of the given is:",len(string)) #prints the length