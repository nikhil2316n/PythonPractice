nums=[-1,0,1,2,-1,-4]

emp=[]
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if nums[i]+nums[j]+nums[k]==0 and i!=j!=k:
                lst=[nums[i],nums[j],nums[k]]
                print(lst)

                


            
