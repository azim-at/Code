email = "azeem.talikoti@gmail.com"
old = "gmail.com"
new = "outlook.com"
newEmail = ""

newList = email.split('@')
for i in newList:
    if i == old:
        newEmail = email.replace(old, new)
print("old email:",email)
print("new email:",newEmail)