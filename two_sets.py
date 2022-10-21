
n = int(input())
s = (n * (n + 1)) // 2

if s % 2 == 0:
    m=(n * (n + 1)) // 4
    a=[]
    b=[]
    for i in range(n,0,-1):
        if i<=m:
            a.append(i)
            m-=i
        else:
            b.append(i)

    print("YES")
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)

else:
    print("NO")