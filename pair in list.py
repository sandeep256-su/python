#how many pairs are present in a list

l=[1,2,3,4,1,2,3,4,5,7,6]
s=set(l)
x=list(s)
count=0
for i in range (0,len(x)):
  z=l.count(x[i])
  if z%2!=0:
    count+=(z//2)
  else:
    count+=z//2
print(count)
