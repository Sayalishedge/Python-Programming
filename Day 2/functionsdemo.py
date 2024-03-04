#display menu and accept choice

def factorial(n):
    '''
    this is factorial function , it accepts one number
    and return factorial
'''
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

def checkprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True

def printtable(n):
    #to find the table of a number
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")    

choice=0
import sys
while choice!=4:
    choice=int(input("""1.factorial
    2.check prime
    3. print table
    4. exit"""))
    if choice!=4:
        n=int(input("enter number"))
    if choice==1:
        ans=factorial(n)
        print(f"Factorial: {ans}")
    elif choice==2:
        status=checkprime(n)
        #if the stats is True
        if(status):
            print("the number is prime")
        else:
            print("the number is not prime")
    elif choice==3:
        printtable(n)
    elif choice==4:
        print("Thank you for visiting....")
        #exit function will exit the program forcefully
        #sys.exit(0)
    else:
        print("wrong choice")












