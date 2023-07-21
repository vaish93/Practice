def swapIfGreater(arr1,arr2,indx1,indx2):
   if arr1[indx1] > arr2[indx2]:
       arr1[indx1],arr2[indx2] = arr2[indx2],arr1[indx1]

arr1= [1,3,6,9]  
arr2 = [2,7,8,24,56]

m = len(arr1)
n = len(arr2)

mylen = n+m

#gap method

gap = (mylen // 2) + (mylen % 2)

while gap>0:
    left = 0
    right = left + gap
    while right < mylen:
        if left < m and right >= m:
            swapIfGreater(arr1,arr2,left,right-m)
        elif left >= m:
            swapIfGreater(arr2,arr2,left-m,right-m)
        else:
            swapIfGreater(arr1,arr1,left,right)
        left+=1
        right+=1
    
    if gap == 1 :
        break
    gap = (gap // 2) + (gap % 2)

print(arr1,arr2)





