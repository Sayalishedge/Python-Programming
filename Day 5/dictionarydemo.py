d1={'a':10,'b':20}
d2={'b':200,'c':30}
#add all values of d2 in d1, it will change d1
#d1.update(d2)
#print(d1,d2)

#create new dictionary d3 by copying all keys of d1 and d2, and if
# keys are same then the d1's value will be overwritten by d2 values
d3={**d1,**d2}
print(d3,d1,d2)

#create a new dictionary by adding every value from list as key
#value of all keys will be None
lst=[12,13,14]
d=dict.fromkeys(lst)
print(d)

#create a new dictionary by adding every value from list as key
#value of all keys will be 200
d11=dict.fromkeys(lst,200)
print(d11)

#create a new dictionary by adding every value from list as key
#value of all keys will be [200,100,23,45]
d11=dict.fromkeys(lst,[200,100,23,45])
print(d11)

d1={'DTISS':100,'DBDA':60}
#add a new key
d1['DAC']=240

#to overwrite the value of existing key
d1['DBDA']=100
print(d1)

#delete key-value pair if key exists and returns its value,
#otherwise throw exception
v=d1.pop('DTISS')
print(v)

#delete key-value pair if key exists and returns its value,
#otherwise returns the default value
v=d1.pop('DTISS',-1)
print(v)

#delete last key-value pair
k,v=d1.popitem()
print(k,v)









