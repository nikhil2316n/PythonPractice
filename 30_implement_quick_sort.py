def quickSort(arr,start,end):

    if start<end:
    
        pivot=partition(arr,start,end)

        quickSort(arr,start,pivot-1)
        quickSort(arr,pivot+1,end)



def partition(arr,start,end):
    
    i=start-1
    pivot=arr[end]
    if start<end:
        
        for j in range(start,len(arr)):

            if(arr[j]<pivot):
                i+=1
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp

        i+=1
        arr[i] , arr[end] = arr[end],arr[i]
        
    return i

arr = [8, 3, 1, 7, 0, 10, 22,56,-1,2,67,93,19993]
quickSort(arr, 0, len(arr)-1)
print(arr)