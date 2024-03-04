#course Manage System
#[("DBDA",60),("DAC",240)]

clist=[("DBDA",60),("DAC",240)]

#add new course in the clist
def addnewcourse():
    cname=input("enter course name")
    capacity=int(input("enter capacity"))
    clist.append((cname,capacity))
    return True

#display all courses from the clist, if no list is passed,
#otherwise display data from the list which is passed
def displayall(clst=clist):
    for cname,cap in clst:
        print(f"{cname} --->{cap}")

#it search the course name, and return position,course name, and capacity
#if found, otherwise return None
def searchByName(cnm):
    for pos,x in enumerate(clist):  #[(0,(DBDA,60))]
       if x[0]==cnm:
           return pos,x[0],x[1]
    return None,None,None

#serach data, if found ask user for confirmation, if user says yes
#then delete it ,otherwise keep as it is
def deleteByName(cnm):
    pos,cname,cap=searchByName(cnm)
    if cname!=None:
        ans=input(f"Do you want to delete {cname}")
        if ans=="y":
            clist.remove((cname,cap))
            return 1
        else:
            return 2
    else:
        return 3

#modify the old coursename with new course name, if foud
#before modifying ask user, whtehr to modify or not
def updateName(oldcnm,newcnm):
    pos,cname,cap=searchByName(oldcnm)
    if cname!=None:
        ans=input(f"Do you want to update {cname}")
        if ans=="y":
            lst=list((cname,cap))
            lst[0]=newcnm
            x=tuple(lst)
            print(x)
            clist[pos]=x
            return 1
        else:
            return 2
    else:
        return 3

#it will display all courses with capacity > given capacity
def displayByCapacity(cap):
    lst=[]
    for cname,capacity in clist:
        if capacity>cap:
            lst.append((cname,capacity))
    if len(lst)>0:
        return lst
    else:
        return None
    
choice=0
while choice!=7:
    choice=int(input("""
    1. add new course
    2. delete the course
    3. modify capacity of the course
    4. modify coursename
    5. display all courses
    6. display all courses with > than given capacity
    7. exit
    """))
    match choice:
        case 1:
           addnewcourse()
        case 2:
           cnm=input("enter coursename to delete")
           status=deleteByName(cnm)
           if status==1:
               print("course deleted successfully")
           elif status==2:
                print("course found but not deleted")
           else:
               print("not found")
        case 4:
           oldcnm=input("enter oldcname")
           newcnm=input("enter oldcname")
           status=updateName(oldcnm,newcnm)
           if status==1:
               print("course updated successfully")
           elif status==2:
                print("course found but not updated")
           else:
               print("not found")
        case 5:
            displayall()
        case 6:
            cap=int(input("enter capacity"))
            lst=displayByCapacity(cap)
            if lst!=None:
                displayall(lst)
            else:
                print("not found")
        case 7:
            print("Thank you for visiting....")

            
               
    
