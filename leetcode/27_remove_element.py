class Solution(object):
    def removeElement(self, nums, val):
        for i in nums:
            if i == val:
                nums.remove(i)

nums = [0,1,2,2,3,0,4,2]

obj=Solution()
obj.removeElement(nums,2)