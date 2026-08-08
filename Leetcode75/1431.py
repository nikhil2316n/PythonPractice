ca = [4,2,1,1,2]
ex = 1
res=[]
max1=max(ca)
for i in range(len(ca)):
    sum=ca[i]+ex
    if sum>=max1:
        res.append(True)
        
    else:
        res.append(False)
    sum=0

print(res)