import re
s="something is there somewhere"
lst=re.findall("s.*?e",s,re.I|re.M)
if lst!=None:
    print(lst)
else:
    print("not found")

lst=re.finditer("s.*?e",s,re.I|re.M)
if lst!=None:
    for m in lst:
        print(m.group())
        print(m.span())
else:
    print("not found")

lst=re.sub("s.*?e","any",s,flags=re.I|re.M,count=2)
print(lst)

