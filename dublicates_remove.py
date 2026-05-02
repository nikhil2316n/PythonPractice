nums = [0,0,1,1,1,2,2,3,3,4]

lgt=len(nums)-1
i=0

while(i<lgt):
    j=i+1
    if(nums[i]==nums[j]):
        nums.append("_")
        nums.pop(j)

    else:
        i+=1
        j+=1

print(nums)