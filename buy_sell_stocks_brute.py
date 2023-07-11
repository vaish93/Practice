arr = [8,1,5,6,11,20,3]

n = len(arr)
maxpro =0

for i in range(n):
    for j in range(i+1,n):
        if arr[j]>arr[i]:
            maxpro = max((arr[j]-arr[i]),maxpro)

print(maxpro)
