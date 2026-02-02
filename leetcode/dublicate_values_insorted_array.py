nums = [0,0,1,1,1,2,2,3,3,4]
count=0

for i in range(len(nums)):
    for j in range(i+1,len(nums)):

        if(nums[i]==nums[j]):
            count+=1
            x=nums[j-1]
            nums.remove(x)

print(count)
print(nums)

