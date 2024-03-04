a=12,"sddd",34,56  #packing of the tuple
b=(10,20,30) #packing of the tuple
print(a,b)
##x=b[0]
##y=b[1]
##z=b[2]
#the number of variables on the LHS of = sholud be
#same as length of the tuple
x,y,z=b     #unpacking of the tuple

c=23,  #c tuple of size 1 , is needed
print(type(c))

#swap the 2 numbers
a=34
b=55
print("Before :",a,b)
a,b=b,a
print("After :",a,b)

def f1(a,b):
    a=a+10
    b=b+20
    return a,b

x=f1(2,3)
print(x)
x,y=f1(2,3)
print(x,y)





