
def del_dubli(arr):

    

    for i in range(len(arr)):

        j=len(arr)-1
        while j >i:
            if arr[i]==arr[j]:
                arr.pop(j)
            j=j-1
    return arr

arr=[1,3,4,2,1,7,8,6,5,3,2,0,1,2,3,5,6]
print(del_dubli(arr))
