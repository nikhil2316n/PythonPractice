# Dynamic sliding window

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]

arr=[1,1,1,0,0,0,1,1,1,1,0]
k=2
left=0
maxone=0
lgt=0
for right in range(len(arr)):
    if(arr[right]==0):
        k-=1
    while(k<0):
        if(arr[left]==0): k+=1
        left+=1
    maxone=max(maxone,right-left+1)

print(maxone)