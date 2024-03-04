# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:43:37 2023

@author: anilk
"""
from personclass import *
elist={'Raj1':SalariedEmp('Rajan','game','mgr',23456),
       'Rev2':ContractEmp('Revati','UX','designer',34,5000),
       'Rev3':SalariedEmp('Revati','game','mgr',23456)}
def addnewemployee(ch):
    pname=input("enetr name")
    dt=input("enetr department")
    ds=input("enetr designation")
    if ch==1:
        sal=float(input("enter sal"))
        e=SalariedEmp(pname,dt,ds,sal)
    else:
        hrs=int(input("enter hours"))
        charges=float(input("enetr charges"))
        e=ContractEmp(pname,dt,ds,hrs,charges)
    elist[e.get_pid()]=e
    
def displayall(elst=elist):
    for emp in elst.values():
        print(emp)
        
def searchByid(pid):
    v=elist.get(pid)
    return v

def searchByName(pname):
    employees={}
    for k,v in elist.items():
        if v.get_pname()==pname:
           print(k)
           employees[k]=v 
    if len(employees)>0:
        return employees
    else:
        return None

def sortBySal():
    lst=list(elist.values())
    lst.sort(key=lambda ob:ob.get_sal() if isinstance(ob, SalariedEmp) else ob.get_charges())
    for emp in lst:
        print(emp)
        
        
def calculatenetsal(pid):
    emp=searchByid(pid)
    if emp!=None:
        return emp.calculateSal()
    else:
        return None
def modifySal(pid,sal):
    emp=searchByid(pid)
    if emp!=None:
        if isinstance(emp, SalariedEmp):
            emp.set_sal(sal)
        elif isinstance(emp,ContractEmp):
            emp.set_charges(sal)
        return True
    else:
        return False
choice=0
while choice!=9:
    choice=int(input("""
                     1. Add new employee
                     2. delete the employee
                     3. modify employee salary
                     4. display all
                     5. display by id
                     6. display by name
                     7. sort on sal
                     8. calaculate net salary
                     9. exit
                     
                     """))
    match choice:
        case 1:
            ch=int(input("""1. salaried employee
                         2. contract employee"""))
            addnewemployee(ch)
        case 2:
            pass
        case 3:
            pid=input("enetr pid")
            sal=float(input("enter salary"))
            status=modifySal(pid,sal)
            if status:
                print("modified successfully")
            else:
                print("not found")
        case 4:
            displayall()
        case 5:
            pid=input("enter id to search");
            emp=searchByid(pid)
            if emp!=None:
                print(emp)
            else:
                print("not found")
        case 6:
            pname=input("enetr nameto search")
            elst=searchByName(pname)
            if elst!=None:
                displayall(elst)
            else:
                print("Not found")
            
        case 7:
            sortBySal()
        case 8:
            pid=input("enetr pid")
            sal=calculatenetsal(pid)
            if sal!=None:
                print(f"{pid} ---->{sal}")
            else:
                print("not found")
        case 9:
            print("Thank you for visiting.....")    
        case _:
            print("wrong choice")
    
    
    
    
    