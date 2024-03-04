from coursemoduledict import *
choice=0
while choice!=7:
    choice=int(input("""
    1. add new course
    2. delete a course
    3. modify coursename
    4. modify capacity
    5. display all
    6. display all courses with capacity>given capacity
    7. exit
    """))
    match choice:
        case 1:
            status=addnewcourse()
            if status:
                print("new course added")
            else:
                print("course exists")
        case 2:
            cname=input("enter the course to delete")
            status=deleteByName(cname)
            if status==1:
                print("found and deleted successfully")
            elif status==2:
                print("found but not deleted")
            else:
                print("not found")
        case 3:
            cname=input("enter the course to modify")
            newname=input("enter the course to modify")
            status=modifyByName(cname,newname)
            if status==1:
                print("found and modified successfully")
            elif status==2:
                print("found but not modified")
            else:
                print("not found")
        case 4:
            cname=input("enter the course to modify")
            ncapacity=input("enter the new capacity to modify")
            status=modifyCapacity(cname,ncapacity)
            if status==1:
                print("found and modified successfully")
            elif status==2:
                print("found but not modified")
            else:
                print("not found")
        case 5:
            displayall()
        case 6:
            capacity=int(input("enetr capacity to search"))
            d=searchByCapacity(capacity)
            if d!=None: 
                displayall(d)
            else:
                print("not found")
        case 7:
            print("Thank you for visiting")
        case _:
            print("wrong choice")


        
