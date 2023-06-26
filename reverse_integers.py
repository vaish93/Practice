#reverse integers in python


input = 12345

inp_ls = list(str(input))
print(inp_ls)
output = []

for num in inp_ls:
    output.insert(0,num)

print("".join(output))  #54321