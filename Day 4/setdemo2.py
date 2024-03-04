s={12,1,31,23}
s.add(14)

s.add("xyz")
s.add((12,13,14))
print(s,len(s))
#set stores only imutable values
#s.add([11,12,13]) #error,
#to add 3 different values, from the list, in the set
s.update([100,33,45])
print(s,len(s))

#delete a value from the set randomly
x=s.pop()
print(x,s)

#to delete a particular value if exists
x=s.remove(100)
print(x,s)
x=s.remove(100)
print(x,s)









