num=45
while True:
    try:
        n1=int(input("enetr number"))
        if n1==num:
            print("yepee, You got the number!!!")
            break
        else:
            raise ValueError("Opps, you lost the attempt!!")
    except ValueError as e:
        print(e)

