####### 1
mystring = "Vaishali is a Automation tester"

#Input: s = “geeks quiz practice code” 
#Output: s = “code practice quiz geeks”

list1 = mystring.split(" ")
list2 = []

for word in list1:
    list2.insert(0,word)

print(list2)
output = " ".join(list2)
print(output)  #tester Automation a is Vaishali

############ 2

#Input: s =  "code” 
#Output: s = “edoc”

mystring_1 = "code"
list_1 = list(mystring_1)
list_2 = []

for letter in list_1:
    list_2.insert(0,letter)

output_1 = "".join(list_2)
print(output_1)  #edoc

############ 3



#Input: s =  "code is easy” 
#Output: s = “edoc si ysae ”

mystring3 = "code is easy"
list_4 = mystring3.split(" ")

mylen = len(list_4)
output=[]

for word in list_4:
    myword_list = list(word)
    reverse_words = []
    for letter in myword_list:
        reverse_words.insert(0,letter)
        word = "".join(reverse_words)
    output.append(word)
print(output)

final_ = " ".join(output)
print(final_)   #edoc si ysae





