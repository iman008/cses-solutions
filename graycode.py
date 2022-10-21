n=int(input())-1

arr=['0','1']
arrp=[]
for i in range(n):
    arrp=arr[::-1]
    arr=arr+arrp
    le=len(arr)//2
    for i in range(le):
        arr[i]=arr[i]+'0'
    for i in range(le,2*le):
        arr[i]=arr[i]+'1'
        


for i in (arr):
    print(i)