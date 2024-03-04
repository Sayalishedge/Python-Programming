lst=[12,13,14]
lst1=[12,4,"xxx",[120,220,320]]
#calculate length of the list
print(len(lst1))
#retrieve the value at the particular index position
print("Before",lst1[2])
#overwrite the value at the particular index position
lst1[2]=3000
print("After",lst1[2])

lst.append(100)
lst.append("xxxx")
lst.append([1,2,3,4])
print(len(lst))
print(lst)
print(lst[5][1])
print(lst[5].append(10))
print(lst)



lst.extend("string")
lst.extend([12,13,14])
print(lst)

lst=[12,11,13,14]
#insert data at 2 nd position, and all values from 2nd
#position onward will be shifted on right
lst.insert(2,4500)
print(lst)
#since 10 is beyond the limit of the length of the list, data will
#added at the last position
lst.insert(10,4500)
print(lst)

#check whether 13 exists in the list or not
print(13 in lst)
#check whether b does not exists in the list or not
print("b" not in "testing a data")






