'''adding each element of list as a list the again
with 2 element as a list the all element as list'''
def func(arr):
    add=0
    d=[]
    e=0
    for i in range(0,len(arr)):
        add+=arr[i]
    mul=2*add


    for j in range(0,len(arr)-1):
        k=j+1
        while k<len(arr):
            ad=arr[j]+arr[k]
            d.append(ad)
            break

   


    for l in range(0,len(d)):
        e+=d[l]
    sum=mul+e
    return sum
        
array=[3,-2,1,-5,3,8]
result=func(array)
print(result)
        
