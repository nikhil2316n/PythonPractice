nums=[-1,0,1,2,-1,-4]

emp=set()
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                triplets=tuple(sorted([nums[i],nums[j],nums[k]]))
                emp.add(triplets)

lst=[]

for t in emp:
    lst.append(list(t))

print(lst)

                


            
