#bubble sort and 3 highest no.
l=[2,4,8,1,7,2,6]
z=len(l)
b=0
for i in range(0,z):
    if z+1:
        break
    else:
        if l[i]>l[i+1]:
            temp=l[i+1]
            l[i+1]=l[i]
            l[i]=temp
    
print(l)            
m=l[::-1]
print(m[2])
 

            
    
