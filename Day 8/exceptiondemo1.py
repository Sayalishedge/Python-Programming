def divide(x,y):
    try:
        ans=x/y
        return ans
    except ZeroDivisionError as e:
        print(e)
        raise e  #rethrow the exception

try:
    x=int(input("enter number"))
    y=int(input("enter number"))
    ans=divide(x,y)
    b=10+ans
        
    
except ValueError:
    print("error occured, pls enter number")
except ZeroDivisionError:
    print("error occured, pls enter value other than 0")
except Exception as e:
    print("error ocuured",e) 
finally:
    print("in finally block")

