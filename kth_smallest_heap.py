import heapq

arr = [3,2,7,1,78,23]
k = 3

a = []

N= len(arr)

for i in range(N):
    heapq.heappush(a,arr[i])

f=k-1

while f>0:
    heapq.heappop(a)
    f-=1


print("3rd smallest element" ,a[0])


