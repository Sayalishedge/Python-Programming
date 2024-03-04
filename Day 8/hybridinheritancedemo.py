class A:
    def __init__(self,a1=0,a2=0):
        print("in A init")
        self.__a1=a1
        self.__a2=a2
    def __str__(self):
        return f' A1: {self.__a1} A2: {self.__a2}'
class B(A):
    def __init__(self,a1=0,a2=0,b1=0,b2=0):
        print("in B init")
        A.__init__(self,a1,a2)
        self.__b1=b1
        self.__b2=b2
    def __str__(self):
        return A.__str__(self)+f' B1: {self.__b1} B2: {self.__b2}'

class C(A):
    def __init__(self,a1=0,a2=0,c1=0):
        print("in C init")
        A.__init__(self,a1,a2)
        self.__c1=c1
       
    def __str__(self):
        return A.__str__(self)+f' C1: {self.__c1}'
    
    
class D(B,C):
    def __init__(self,a1=0,a2=0,b1=0,b2=0,c1=0,d1=0,d2=0):
        print("in D init")
        B.__init__(self,a1,a2,b1,b2)
        C.__init__(self,a1,a2,c1)
        self.__d1=d1
        self.__d2=d2
        
    def __str__(self):
        return B.__str__(self)+C.__str__(self)+f" D1: {self.__d1} D2: {self.__d2}"
    
    
ob=D(1,2,11,12,31,41,42)
print(ob)       
        
        
        
        
        
    