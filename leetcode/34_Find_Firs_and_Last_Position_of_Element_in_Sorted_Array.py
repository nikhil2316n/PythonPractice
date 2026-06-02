#Binary Search

nums=[1,3,4,4,4,5,6,7,8,9]
target=4


def findstartend(num,target):
    left=0
    right=len(nums)-1
    index=-1
    while(left<=right):
        mid=(left+right)//2
        if(nums[mid]==target):
            index=mid
            right=mid-1
        elif(nums[mid]<target):
            left=mid+1
        else:
            right=mid-1

def findend(num,target):
    left=0
    right=len(nums)-1
    index=-1
    while(left<=right):
        mid=(left+right)//2
        if(nums[mid]==target):
            index=mid
            right=mid-1
        elif(nums[mid]<target):
            left=mid+1
        else:
            right=mid-1
left=findstartend(nums,target)
right=findend(nums,target)

print(left,right)