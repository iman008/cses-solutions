
arr=[]
for i in input():
    arr.append(i)
arr.append('0')
p1=0
lent=0
best=0
for i in range(0,len(arr)):
    if arr[i]==arr[p1]:
        lent=lent+1
    else:
        best=max(lent,best)
        lent=1
        p1=i
print(best)
