import re
s="something is there somewhere"
m=re.search("t.*?e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")

m=re.match("t.*?e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")

#it always checks the pattern anywhere in the string
m=re.search("s.*?e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")

#it always checks the pattern at the begining
m=re.match("s.*?e",s,re.I|re.M)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")
