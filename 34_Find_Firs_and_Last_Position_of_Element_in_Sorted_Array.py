nums = [5,7,7,8,8,10]
target = 8
left=0
newarr=[]
right=len(nums)-1
while(left<=right):
    if(nums[left]==target):
        newarr.append(left)
    left+=1
    if(nums[right]==target):
        newarr.append(right)
    right-=1