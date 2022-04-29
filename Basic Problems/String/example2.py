#input "azim is a gamer"
#expected output "is gamer"
n = "Azim is a gamer"
newlist = n.split()
a=newlist[1::2]
out =' '.join(a)
print(out)