lst=[12,13,14]
lst1=["Pune","Mumbai","Delhi","Banglore"]
lst2=[45,67,89,45]
#zip it allows to traverse through multiple lists
#simulteneously
for x in zip(lst,lst1):  #[(12,"Pune"),(),()]
    print(x)

for x,y in zip(lst,lst1):  #[(12,"Pune"),(),()]
    print(x,y)


for x,y in enumerate(lst1,100): #[(0,Pune),(1,Mumbai),(2,Delhi)]
    print(x,y)

#without modifying the original list, to iterate
#through the list in the sorted order
for city in sorted(lst1):
    print(city)

#without modifying the original list, to iterate
#through the list in the sorted order, in descending
#order use reverse
for city in sorted(lst1,reverse=True):
    print(city)

print(lst1)

#without changing the original list,
#if you want to navigate through the list,
#in the reverse order
for city in reversed(lst1):
    print(city)






    
    
   

