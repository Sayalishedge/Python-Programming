courses={'DBDA':100,'DTISS':120}
def addnewcourse():
    cname=input("enetr new course")
    capacity=int(input("enetr capacity"))
    v=courses.get(cname,-1)
    #key does not exists
    if v==-1:
        courses[cname]=capacity
        return True
    else:  #key exists
        return False

def displayall(d=courses):
    for k,v in d.items():
        print(f"{k}--->{v}")
        
def searchByCapacity(c):
     result={}  #create empty dictionary
     for k,v in courses.items():
         if v>c:
             result[k]=v  #add key:value in the dictionary
     if len(result)>0:
        return result
     else:
         return None
        
def deleteByName(cname):
    #del(courses[cname])
    #courses.pop(cname,-1)
    v=courses.get(cname,-1)
    if v!=-1:  #check whether found, if found
        ans=input(f"delete {cname} {v}?")
        if ans=='y':
            courses.pop(cname)
            return 1
        else:
            return 2
    else:       #if not found
        return 3
    
def modifyByName(cname,newname):
     v=courses.get(cname,-1)
     if v!=-1:  #check whether found, if found
        ans=input(f"modify {cname} to {newname}?")
        if ans=='y':
            courses.pop(cname)   #delete the existing key
            courses[newname]=v  # add new key-value pair
            return 1
        else:
            return 2
     else:       #if not found
        return 3
def modifyCapacity(cname,ncapacity):
    v=courses.get(cname,-1)
    if v!=-1:  #check whether found, if found
        ans=input(f"modify capacity of {cname} to {newname}?")
        if ans=='y':
            courses[cname]=ncapacity  # add new key-value pair
            return 1
        else:
            return 2
    else:       #if not found
        return 3
