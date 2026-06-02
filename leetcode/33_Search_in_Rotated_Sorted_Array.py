# Input: nums = [4,5,6,7,0,1,2], target = 0
nums=[4,5,6,7,0,1,2]
tgt=0

def Search(nums,tgt):
    for i in range(len(nums)):
        if(nums[i]==tgt):
            return i
    return -1
