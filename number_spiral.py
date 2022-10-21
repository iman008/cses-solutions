def f(m):
    return m**2-m+1

def solve(y,x):
    if y<x:
        if x%2==0:
            return ( f(x)-x+y)
        else :
            return (f(x) +x-y)
    else:
        if y%2==0:
            return f(y)+y-x
        else:
            return f(y) -y+x

n=int(input())

for i in range(n):
    y,x=[int(x) for x in input().split()]
    print(solve(y,  x))