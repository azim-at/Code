import secrets

myList = ["IT IS CERTAIN","YOU MAY RELY ON IT","AS I SEE IT, YES","“OUTLOOK LOOKS GOOD","MOST LIKELY","IT IS DECIDELY SO","WITHOUT A DOUBT","YES, DEFINETLY"]
for z in myList:
    newRand = secrets.choice(myList)
    print(newRand)
    break
    