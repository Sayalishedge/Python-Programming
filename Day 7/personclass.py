from abc import abstractmethod,ABC
class Person:
    #static variable
    count=0
    #static method
    #static method can use only static value, 
    #self is not accessible in static methods
    @staticmethod
    def generateId(pname):
        Person.count=Person.count+1
        return pname[:3]+str(Person.count)
        
    def __init__(self,pname=""):
        self.__pid=Person.generateId(pname)
        self.__pname=pname
        
    def set_pname(self,nm):
        self.__name=nm
    def get_pname(self):
        return self.__pname  
    def get_pid(self):
        return self.__pid  
    def __str__(self):
        return f"Id : {self.__pid} Name: {self.__pname}"
    
class Employee(Person,ABC):
    def __init__(self,pname="",dept="",desg=""):
        super().__init__(pname)
        self.__dept=dept
        self.__desg=desg
        
    def set_dept(self,dt):
        self.dept=dt
    def set_desg(self,ds):
        self.desg=ds    
    def get_dept(self):
        return self.dept
    def get_desg(self):
        return self.desg 
    @abstractmethod
    def calculateSal(self):
        pass
    def __str__(self):
        return super().__str__()+f" Dept : {self.__dept} Desg : {self.__desg}"
    
class SalariedEmp(Employee):
    def __init__(self,pname="",dt="",ds="",sal=0):
        super().__init__(pname,dt,ds)
        self.__sal=sal
        self.__bonus=0.10*sal
    def set_sal(self,s):
        self.__sal=s;
    def set_bonus(self,b):
        self.__bonus=b;    
    def get_bonus(self):
        return self.__bonus;
    def get_sal(self):
        return self.__sal;
    def calculateSal(self):
        return self.__sal++0.10*self.__sal+0.15*self.__sal-0.08*self.__sal+self.__bonus
    def __str__(self):
        return super().__str__()+f" Salary : {self.__sal} Bonus: {self.__bonus}"

class ContractEmp(Employee):
    def __init__(self,pname="",dt="",ds="",hrs=0,charges=0):
        super().__init__(pname,dt,ds)
        self.__hrs=hrs
        self.__charges=charges
    def set_hrs(self,s):
        self.__hrs=s;
    def set_charges(self,b):
        self.__charges=b;    
    def get_hrs(self):
        return self.__hrs;
    def get_charges(self):
        return self.__charges;
    def calculateSal(self):
        return self.__hrs*self.__charges
    def __str__(self):
        return super().__str__()+f" Hrs:  {self.__hrs} Charges: {self.__charges}"    
if __name__=="__main__":
    p1=SalariedEmp("Rajan","Gaming","game designer",345678)
    print(p1)
    p2=ContractEmp("Atharva","UI","UI designer",40,10000)
    print(p2)
