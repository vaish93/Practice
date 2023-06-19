"""
input = "Designed and Developed framework for UI 
Automation having Page Object Model Implementation,Data Driven and TestNG
"""
input_string = """Designed and Developed framework for UI 
                    Automation having Page Object Model Implementation , Data Driven and TestNG"""
my_list = input_string.split(" ")
len_list =[]
for word in my_list:
    word_len = len(word)
    len_list.append(word_len)
print(len_list)
max_len = max(len_list)
print(max_len)

for word_1 in my_list:
    word_1_len = len(word_1)
    if max_len == word_1_len:
        print("largest word : " ,word_1)



