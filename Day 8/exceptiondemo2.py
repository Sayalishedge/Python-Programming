#user defined exception
class PasswordWrong(Exception):
    def __init__(self,msg="error occur"):
        self.__msg=msg
    def __str__(self):
        return self.__msg

details={'user1':'user1','admin':'admin'}
for i in range(3):
    try:
        uname=input("enetr username")
        passwd=input("enetr password")
        if details[uname]==passwd:
            print("valid user")
        else:
            raise PasswordWrong("credentials are wrong")
        break
    except (KeyError,PasswordWrong) as e:
        print("wrong data",e)
else:
    print("pls contact admin, your acoount is blocked")
    