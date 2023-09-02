text = "mango red  yellow red mango red"

d= dict()

words = text.split()
for word in words:
    if word in d:
        d[word] +=1
    else:
        d[word] =1
        
        
print(d)



{'mango': 2, 'red': 3, 'yellow': 1}
