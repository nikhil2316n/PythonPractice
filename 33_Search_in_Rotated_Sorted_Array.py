# Input: nums = [4,5,6,7,0,1,2], target = 0
nums=[4,5,6,7,0,1,2]
tgt=0
globalsmall=float('inf')
for i in range(len(nums)):
    globalsmall=min(globalsmall,nums[i])

x=0
for j in range(len(nums)):
    if nums[j]==globalsmall:
        x=j
        break
newarr=nums[x:]+nums[:x]
print(newarr)