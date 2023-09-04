mystr = "Vaishali is a Automation tester"
list1 = mystr.split(" ")
len_mystr = len(list1)
print(len_mystr)
output = ""
for i in range(len_mystr):
    if i%2 == 1:
        word = list1[i]
        list2 = list(word)
        rev_word=[]
        for letter in list2:
            rev_word.insert(0,letter)

        rev_word_final = "".join(rev_word)
    else:
        rev_word_final =  list1[i]
    output = output + " " + rev_word_final
    #output = f'{output,rev_word_final}'
print(output)


#ilahsiav is na automation retset
