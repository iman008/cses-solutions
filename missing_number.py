n=int(input())
arr=[int(x) for x in input().split()]
s=n*(n+1)/2
for i in arr:
    s-=i
print(int(s))