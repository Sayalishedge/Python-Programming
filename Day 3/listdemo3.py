#genarate list to add 10 numbers in it
lst=[]
for i in range(7):
    num=int(input("enter number"))
    lst.append(num)
print(lst)

#to delete the data from the end
print("pop last value",lst.pop())
print("pop from 3 rd index position value",lst.pop(3))

#to delete by value 14 if found
if 14 in lst:
    print("remove 14",lst.remove(14))
