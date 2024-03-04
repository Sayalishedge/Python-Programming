lst=[12,4,35,2,5,6,7,10,26,25]
lst1=[]
for num in lst:
    if num%5==0:
        lst1.append(num)
print(lst1)

#it will work same as the for loop written above
lst1=list(filter(lambda num:num%5==0 and num>7,lst))

lst1=["xxxx","python","linux","OS","perl"]
#to find all string with length <=4
lst2=list(filter(lambda s:len(s)<=4,lst1))
print(lst2)

lst=[2,4,6,3,8]
lst2=list(map(lambda num:num*num,lst))
print(lst2)

#find the country code, it is first 3 characters
country=["INDIA","UK","RUSSIA","US"]
lst2=list(map(lambda c:c[:3],country))
print(lst2)
lst=[2,4,6,3,8]
import functools
ans=functools.reduce(lambda acc,num:acc+num,lst)
print("addition :",ans)

#find maximum number from the lst
ans=functools.reduce(lambda acc,num:acc if acc>num else num,lst)

#ternary operator in python
#acc if acc>num else num  (acc>num?acc:num)

print("sum of numbers",sum(lst))
print("Maximum number",max(lst))
print("minimum number:",min(lst))

lst=["Python","Perl","linux","OS"]
ans=functools.reduce(lambda acc,num:acc+num,lst,"xxxxx")
print(ans)

