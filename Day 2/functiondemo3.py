#x and y are manditory parameters
#z and p are optional parameters
def myf1(x,y,z=4,p=23):
    print(x,y,z,p)

def myf2(a=12,b=34,c=45):
    print(a,b,c)

myf2()
myf2(100)
myf2(1,2,3)


myf1(11,12)
#values are assigned to parameters by position
myf1(100,200,300,400)
myf1(10,20,p=50,z=45)
myf1(p=11,y=22,z=33,x=55)
a=34j
print(type(a))

