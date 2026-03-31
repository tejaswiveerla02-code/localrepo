n= int(input())
arr=list(map(int,input().split()))
freq={}

for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
        
q= int(input())
queries=[]
for p in range(q):
    queries.append(int(input()))
res=[]
for x in queries:
    res.append(freq.get(x,0))
for r in res:
    print(r)
    