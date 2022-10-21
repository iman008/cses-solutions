n=int(input())
if n==2 or n==3:
    print("NO SOLUTION")
if n==1:
    print(1)
else:
    for i in range(1,n+1):
        if i%2==0:
            print(i,end=" ")
    for i in range(1,n+1):
        if i%2==1:
            print(i,end=" ")
