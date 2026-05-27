arr=[1,3,5,7,9,10,12,14,17,19,21,55]
tgt=12
def binarySearch(arr,tgt):
    left=0
    right=len(arr)-1
    while(left<=tgt):
        mid=(left+right)//2
        if(arr[mid]==tgt):
            return mid
        elif(arr[mid]<tgt):
            left=mid+1
        else:
            right=mid-1
    return -1

print(binarySearch(arr,tgt))