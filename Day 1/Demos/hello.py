print("hello world!!")
a=5
a=int(input("enter number1"))
b=int(input("enter number2"))
print(a+b)
if a<b:
    print(str(a)+"is minimum")
    print("%d is minimum"%(a))
    print(f"{a} is minimum {a+b}")
    print("{0} is minimum, {1} is maximum".format(a,b))
else:
    print(str(b)+"is minimum")
    print("%d is minimum"%(b))
    print(f"{b} is minimum {a+b}")
    print("{0} is minimum, {1} is maximum".format(a,b))
    
print("outside if")