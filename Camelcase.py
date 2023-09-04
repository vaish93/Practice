myline = "my name is vaishali"

mylist = myline.split(" ")

mylist1 = []

for i in range(len(mylist)):
    letterlist = list(mylist[i])
    letters = []
    for i in range(len(letterlist)):
        if i == 0:
            d = letterlist[i].upper()  
        else: 
            d= letterlist[i]
        letters.append(d)
    final_word = "".join(letters)
    mylist1.insert(0,final_word)
print(" ".join(mylist1))


#Tester Automation An Is Vaishali
