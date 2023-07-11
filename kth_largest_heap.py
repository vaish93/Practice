import heapq

arr = [8,3,6,1,4,90,23]

N = len(arr)  
k = 2
a = []

for i in range(N):
    heapq.heappush(a,-arr[i])

f = k-1

while f>0:
    heapq.heappop(a)
    f-=1

print("2nd largest element",-a[0])

