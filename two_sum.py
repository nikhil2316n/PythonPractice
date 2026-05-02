#Two pointer problem

nums=[1,2,3,5,7,10,11,15]
target=15

# for i in range(0,len(nums)):
#     for j in range(0,len(nums)):
#         sum1=nums[i]+nums[j]
#         print(nums[i],nums[j])
#         if sum1 ==target:
#             print(i,j)
        

left=0
right=len(nums)-1
while(left<right):
    current_sum=nums[left]+nums[right]
    if(current_sum==target):
        print(left,right)
        break

    elif(current_sum>target):
        right=right-1
    else:
        left=left+1