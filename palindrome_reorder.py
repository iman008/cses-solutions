from collections import defaultdict


str=str(input())

freq=defaultdict(int)

for i in range(len(str)):
    freq[str[i]]+=1
oddcount=0
oddchar=""
for i in freq:
    if freq[i]%2==1:
        oddcount+=1
        oddchar=i



if ((oddcount==1 and len(str)%2==0) or oddcount>1):
    print("NO SOLUTION")
else:
    first=""
    second=""

    for x in sorted(freq.keys()):
        s=(freq[x]//2)*x
        first=first+s
        second=s+second

    if oddcount==1:
        print(first + oddchar + second)
    else:
        print(first + second)