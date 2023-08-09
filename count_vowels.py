mystring = "VAISHALI"
vowels = "aeiou"
print(mystring)
mystring = mystring.casefold()
print(mystring)

count = {}.fromkeys(vowels,0)
print(count)

for letter in mystring:
    if letter in count:
        count[letter] +=1

print(count)  #{a:2,e:0.....}
