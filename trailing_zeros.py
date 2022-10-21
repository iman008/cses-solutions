n=int(input())

i=5
res=0
while n/i>=1:
    res += n//i
    i*=5
print(int(res))
