#matrix creation
a=[]
c=[]
m=int(input('enter the value of rows:'))
n=int(input('enter the value of columns:'))
i=0
while i<m:
    b=[]
    j=0
    while j<n:
        print('enter the value:')
        a=int(input())
        b.append(a)
        j+=1
    c.append(b)
    i+=1
print(c)
