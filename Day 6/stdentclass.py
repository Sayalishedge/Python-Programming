# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:14:24 2023

@author: anilk
"""

class Student:
    #constructor 
    def __init__(self,sid=0,snm="",addr="",m1=0):
        self.__sid=sid
        self.__sname=snm
        self.__addr=addr
        self._m1=m1
        
    #setter and getter methods    
    def set_sid(self,sid):
        self.__sid=sid
    def set_sname(self,snm):
        self.__sname=snm
    def set_addr(self,addr):
        self.__addr=addr
    def set_m1(self,m1):
        self._m1=m1
    def get_sid(self):
        return self.__sid
    def get_sname(self):
        return self.__sname
    def get_addr(self):
        return self.__addr
    def get_m1(self):
        return self._m1
    def __str__(self):
        return f"Sid : {self.__sid} Name: {self.__sname} address: {self.__addr}"
    
class MscStudent(Student):
    def __init__(self,sid=0,sname="",addr="",m1=0,m2=0,m3=0,spsub=0):
        #Student.__init__(self,sid,sname,addr)
        #explicit call is needed for parent constructor
        super().__init__(sid,sname,addr,m1)
        self.__m2=m2
        self.__m3=m3
        self.__spsub=spsub
    def set_m2(self,m2=0):
        self.__m2=m2
    def set_m3(self, m3=0):
        self.__m3=m3
    def set_spsub(self,s=0):
        self.spsub=s
    def get_m2(self):
        return self.__m2
    def get_m3(self):
        return self.__m3
    def get_spsub(self,s=0):
        return self.spsub
    def calculategradeMSC(self):
        return (self._m1+self.__m2+self.__m3+self.__spsub)/100
    def __str__(self):
        return super().__str__()+f" M2 : {self.__m2} M3:{self.__m3} sp. sub:{self.__spsub} "
     
    
class PhdStudent(Student):
    def __init__(self,sid=0,sname="",addr="",m1=0,m2=0,thesname="", tmks=0):
        #Student.__init__(self,sid,sname,addr)
        #explicit call is needed for parent constructor
        super().__init__(sid,sname,addr,m1)
        self.__m2=m2
        self.__thesname=thesname
        self.__thesmarks=tmks
    def set_m2(self,m2=0):
        self.__m2=m2
    def set_thesname(self, nm=""):
        self.__thesname=nm
    def set_thesmarks(self,s=0):
        self.___thmks=s
    def get_m3(self):
        return self.__m3
    def get_thename(self):
        return self.__thesname
    def get_themarks(self,s=0):
        return self.thesmarks
    def __str__(self):
        return super().__str__()+f" M2 : {self.__m2} thes name:{self.__thesname} thes marks {self.__thesmarks} "
    def calculategradePHD(self):
        return (self._m1+self.__m2+self.__thesmarks)/100    
if __name__=="__main__":
     s1=Student(12,"Rajan","Baner",99)
     print(s1)
     print(s1.get_sname())
     print(s1._m1)
     s1=PhdStudent(12,"Rajan","Baner",99,88,"xxxxx",78)
     print(s1)
     s1=MscStudent(12,"Rajan","Baner",99,88,78,78)
     print(s1)