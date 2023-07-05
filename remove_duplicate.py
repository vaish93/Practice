str = "vvaaisshhu"

result1 = "".join(set(str))
print(result1)   #without order


t = ""

for i in str:
    if i in t:
        pass
    else:
        t = t+i


print(t)  #withorder