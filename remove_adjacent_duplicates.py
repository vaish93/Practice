str = "cabbkggy"
ls = []
i=0

while i<len(str):
   if(len(ls)!=0 and (ls[-1]==str[i])):
        i+=1
        ls.pop(-1)
   else:
       ls.append(str[i])
       i+=1

print("".join(ls))


#caky
    





