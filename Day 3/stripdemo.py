s="asdfsssdddaaffrrThere is stringdddssssaaaa"
news=s.strip("asdfr")
print(news)
news=s.lstrip("asdfr")
print("left stip",news)
news=s.rstrip("asdfr")
print("right strip: ",news)

data="this is line\n"
print("before:",data)
data=data.rstrip("\n")
print("after", data)


acnum="XXXX1234XXXX"
print(acnum.strip("X"))
