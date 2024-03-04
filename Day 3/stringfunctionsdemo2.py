s="This is my cat, where is your cat, the cat is cute"
pos=s.index("cat")
print("position: ",pos)
pos=s.index("cat",pos+1)
print("position: ",pos)
pos=s.index("cat",pos+1)
print("position: ",pos)
#pos=s.index("cat",pos+1)
#print("position: ",pos)

pos=s.rindex("cat")
print("rindex position: ",pos)
