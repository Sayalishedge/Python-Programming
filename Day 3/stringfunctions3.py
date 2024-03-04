s="1203,Sushrut,MANAGER,80000"
lst=s.split(",")
print(lst)
##combine all the words separated by :
s1=":".join(lst)
print(s1)

s2=s.replace(",",":")
print(s2)

    
for ch in s:
    print(ch,end=",")

s="thisisstring1233"
print("isalpha",s.isalpha())
print("isdecimal",s.isdecimal())
print("isalnum",s.isalnum())
