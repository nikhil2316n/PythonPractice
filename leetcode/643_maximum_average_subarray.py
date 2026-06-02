# Find a contiguous subarray whose length is equal to k that has the maximum average 
# value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


nums = [1,12,-5,-6,50,3]
k=4
max_avg=0
sum=0
for i in range(k):
    sum=nums[i]+sum
    avg=sum/4

max_avg=avg
print('hello')
for j in range(1,len(nums)-k+1):
    sum=sum-nums[j-1]+nums[j+3]
    avg=sum/4
    max_avg=max(max_avg,avg)
print(max_avg)