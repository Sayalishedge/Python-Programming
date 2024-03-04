import re
s="this is home"
m=re.search("^(\w+)\s(\w+)\s\w+$",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
    print(m.group(1))
    print(m.span(1))
    print(m.group(2))
    print(m.span(2))
else:
    print("not found")

myreg=re.compile("^(\w+)\s(\w+)\s\w+$",re.I|re.M)
m=myreg.search(s)
if m!=None:
    print(m.group())
    print(m.span())
    print(m.group(1))
    print(m.span(1))
    print(m.group(2))
    print(m.span(2))
else:
    print("not found")


acno="XXXXX1234XXXXX"
m=re.match("X{5}(\d{4})X{5}",acno)
if m!=None:
    print(m.group(1))
else:
    print("not found")

    


           
