#missing numbers in an array

arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]

myset = set(arr)

output = []

for i in range(1,arr[-1]):
    if i not  in myset:
        output.append(i)


print(output)
#[4, 12, 15]