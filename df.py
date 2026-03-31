r1= int(input("enter rows of A:"))
c1= int(input("enter clos in A:"))

r2=int(input("enter rows in ?B:"))
c2= int(input("cols in B"))

a=[]
for i in range(r1):
    row=list(map(int,input().split()))
    a.append(row)
    
b=[]
for i in range(r2):
    row=list(map(int, input().split()))
    b.append(row)
    
res=[]
for i in range(r1):
    row=[]
    for j in range(c2):
        row.append(0)
    res.append(row)
    
for i in range(r1):
    for j in range(c2):
        res[i][j]+=a[i][j]*b[i][j]

for r in res:
    print(r)
       
       
     