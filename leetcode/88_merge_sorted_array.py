nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
ptr1=m-1
ptr2=n-1

index=len(nums1)-1

while(ptr1>=0 and ptr2>=0):
    if(nums1[ptr1]>nums2[ptr2]):
        nums1[index]=nums1[ptr1]
        ptr1-=1
        index-=1
    
    elif(nums1[ptr1]<nums2[ptr2]):
        nums1[index]=nums2[ptr2]
        ptr2-=1
        index-=1
    else:
        nums1[index]=nums1[ptr1]
        index-=1
        ptr1-=1
        nums1[index]=nums2[ptr2]
        ptr2-=1
        index-=1

print(nums1)