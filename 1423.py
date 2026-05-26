arr=[100,2,3,4,5,6,10]
k=3
left=len(arr)-k
right=0
max1=0
sum=0
for i in range(left,len(arr)):
    sum+=arr[i]
max1=sum
while(k>0):
    sum-=arr[left]
    left+=1
    sum+=arr[right]
    right+=1
    k-=1
    max1=max(max1,sum)

print(max1)