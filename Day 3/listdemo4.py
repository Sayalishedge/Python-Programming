lst=[1,2,3,4,5]
#lst1 will point to same memory location
lst1=lst
lst.append(100)
print(lst,lst1)
#it will create a shallow copy of the list
lst2=lst.copy()
lst.append(200)
print(lst,lst1)
print(lst2)

#it will reverse the original list
lst.reverse()
print(lst)

lst=[10,2,3,14,34,9]
lst.sort()
print("after sorting in ascending order",lst)
lst.sort(reverse=True)
print("after sorting in descending order",lst)

lst=["safdsdf","xxxx","aaaa","sdfs"]
lst.sort()
print(lst)
lst=[[12,13],[5,7],[3,34,44]]
lst.sort()
print(lst)
lst.sort(key=lambda ob:ob[1])  #13,7,34
print(lst)
