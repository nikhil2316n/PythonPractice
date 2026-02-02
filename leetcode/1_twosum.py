
num=[1,2,3,4,5]
tgt=9

def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            sum=nums[i]+nums[j]

            if (sum==target):
                
                return [i,j]

print(twosum(num,tgt))