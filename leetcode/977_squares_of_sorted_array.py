
nums = [-4,-1,0,3,10]

class Solution(object):
    def sortedSquares(self,nums):
        res=[0]*len(nums)
        left=0
        right=len(nums)-1
        index=len(nums)-1
        while(left<=right):
            if(abs(nums[left])<abs(nums[right])):
                res[index]=nums[right]**2
                right-=1
            else:
                res[index]=nums[left]**2
                left+=1
            index-=1

        return res
obj = Solution()
print(obj.sortedSquares(nums))