nums=[0,1,0,3,12]

ptr=0

for i in range(0,len(nums)):
    if(nums[i]!=0):
        nums[i],nums[ptr]=nums[ptr],nums[i]
        ptr+=1

print(nums)