lst=[1,2,2,3,3,3,4,4,4,4,4,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]

dic={}
for i in lst:
    if i not in dic:
        dic[i]=lst.count(i)

print(dic)