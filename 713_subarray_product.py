# Given an array of integers nums and an integer k, 
# return the number of contiguous subarrays where the product 
# of all the elements in the subarray is strictly less than k.

nums = [10,5,2,6]
k = 100
count=0
left=0
product=1


for right in range(len(nums)):
    product*=nums[right]
    while(product>=k):
        product/=nums[left]
        left+=1
    
    count+=right-left+1

print(count)