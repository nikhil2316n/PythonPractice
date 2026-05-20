tartget=7
nums=[2,3,1,2,4,3]

print('hello')
left=0
right=0
windows_size=float('inf')
sum1=0
while(right<len(nums)):
    sum1+=nums[right]
    while(sum1>=tartget):
        windows_size=min(right-left+1,windows_size)
        sum1-=nums[left]
        left+=1

    right+=1

print(windows_size)
    