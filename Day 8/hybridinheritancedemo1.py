class A:
    def __init__(self,a1=0,a2=0):
        print("in A init")
        self.__a1=a1
        self.__a2=a2
    def __str__(self):
        return f' A1: {self.__a1} A2: {self.__a2}'
class B(A):
    def __init__(self,b1=0,b2=0,**kwarg):
        print("in B init",kwarg) #a1,a2,c1
        super().__init__(**kwarg)
        self.__b1=b1
        self.__b2=b2
    def __str__(self):
        return super().__str__()+f' B1: {self.__b1} B2: {self.__b2}'

class C(A):
    def __init__(self,c1=0,**kwarg):
        print("in C init")
        super().__init__(**kwarg)  #a1,a2
        self.__c1=c1
       
    def __str__(self):
        return super().__str__()+f' C1: {self.__c1}'
    
    
class D(B,C):
    def __init__(self,d1=0,d2=0,**kwarg):
        print("in D init",kwarg) 
        super().__init__(**kwarg)
        self.__d1=d1
        self.__d2=d2
        
    def __str__(self):
        return super().__str__()+f" D1: {self.__d1} D2: {self.__d2}"
    
    
ob=D(a1=1,a2=2,b1=11,b2=12,c1=21,d1=31,d2=32)
print(ob)  
print(D.mro())     
        
        
        
        
        
    