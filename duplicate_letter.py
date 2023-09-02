text = "Vaishali is an Automation Tester"

d = dict()

text = text.replace(" ","")
print(text)
mylist = list(text)

for letter in mylist:
    if letter in d:
        d[letter] +=1
    else:
        d[letter] = 1
        
for entry,value in d.items():
    if value > 1:
        print(entry , ":" , value)
