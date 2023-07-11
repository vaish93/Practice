n = 100
fact = 1
count = 0

for i in range(1,n+1):
    fact = fact*i

print(fact)

while fact%10 == 0:
    count+=1
    fact //= 10

print(count)