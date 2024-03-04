x=12
y=12
z=x
print(id(x),id(y),id(z))
p=int(input("enetr number"))
print(id(p),p)
x=30
print(id(x),id(y),id(z))

s1="hello"
s2="hello"
s3=input("enter name")
print(id(s1),id(s2),id(s3))
print(s1==s2,s1==s3,s2==s3)
print(s1 is s3,id(s1)==id(s3))
print(s1 is s2,id(s1)==id(s2))
