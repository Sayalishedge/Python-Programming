d1={'a':100,'b':200,'c':30}
#if key exists will return the value, otherwise None
v=d1.get('a')
print(v)

#if key exists will return the value, otherwise -1
v=d1.get('aa',-1)
print(v)
print(d1)
#if key exists will return the value,
#otherwise add new keyvalue pair in the dictionary
v=d1.setdefault('aa',-1)
print(v)
print(d1)

#navigate through the dictionary
for k in d1.keys():
    print(f"{k}--->{d1[k]}")
print("-"*60)
#navigate through the dictionary
for k,v in d1.items():
    print(f"{k}--->{v}")
print("-"*60)
#navigate through the dictionary
for k,v in d1.items():
    if v>50:
        print(f"{k}--->{v}")


