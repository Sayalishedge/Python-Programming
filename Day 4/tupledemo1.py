#to pass variable number of prameters use tuple
#expansion operator
def addition(a,b,*t):
    print(a,b,t)
    s=a+b
    for num in t:
        s=s+num
    return s



ans=addition(1,2)
print(f"Addition : ",ans)
ans=addition(10,20,1,3,423,14)
print(f"Addition : ",ans)
        
