# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

nums = [1,3,5,6]
target = 7

def searchInsert(nums,target):
    left=0
    right=len(nums)-1
    while(left<right):
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
        
    return left

print(searchInsert(nums,target))