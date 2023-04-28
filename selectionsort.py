#selection sort
def selectionsort(l):
    n=len(l)
    for i in range(n-1):
        min_mid=i
        for j in range(i+1,n):
            if l[j]<l[min_mid]:
                min_mid=j
        l[min_mid],l[i]=l[i],l[min_mid]
    return l
a1=selectionsort([2,5,1,8,4])
print(a1)