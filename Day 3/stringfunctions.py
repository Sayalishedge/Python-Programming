s="This is my cat, where is your cat, the cat is cute"
print("uppercase",s.upper())
print("lowercase",s.lower())
##pos=s.find("cat")
##print("the position : ",pos)
##pos=s.find("cat",pos+1)
##print("the position : ",pos)
##pos=s.find("cat",pos+1)
##print("the position : ",pos)
##pos=s.find("cat",pos+1)
##print("the position : ",pos)
#write the code to find all the positions of word cat
pos=s.find("cat")
while pos!=-1:
    print("position : ",pos)
    pos=s.find("cat",pos+1)

pos=s.rfind("cat")
print("position :",pos)
pos=s.rfind("cat",0,pos-1)
print("position :",pos)
