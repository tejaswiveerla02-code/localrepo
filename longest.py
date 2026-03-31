r1= int(input("enter rows in A:"))
c1= int(input("enter cols in A:"))

a=[]
maxCount=0
maxRow=-1
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input()))
    a.append(row)

for j in range(c1):
    count=0
    for i in range(r1):
        if a[i][j]==1:
            count+=1
    if count>maxCount:
        maxCount=count
        maxRow=j
                
print(f"{maxRow}->{maxCount}")
            