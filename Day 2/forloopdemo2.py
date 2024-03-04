#to find factorial of a number
n=int(input("enter number"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"factorial : {fact}")

#to find the table of a number
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

#to check whether given number is prime
flag=False
for i in range(2,n):
    if n%i==0:
        flag=True
        break
if flag:
    print("The number is not prime")
else:
    print("he number is prime")
