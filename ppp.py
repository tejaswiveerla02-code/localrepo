n= int(input())
arr=list(map(int,input().split()))
freq={}

for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
        
q= int(input())
qu=[]
for p in range(q):
    qu.append(int(input()))
res=[]
for x in qu:
    res.append(freq.get(x,0))
for r in res:
    print(r)
    