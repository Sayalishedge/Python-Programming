#finding addition of digits of the number
num=345
n=num
s=0
while n!=0:
    d=n%10   #5   4   3 
    n=n//10   #34 3   0 // is integer division
    s=s+d
print("Addition of",num,"=",s)
print(f"Addition of {num} = {s}")
