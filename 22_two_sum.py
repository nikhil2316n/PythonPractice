arr=[2,7,11,15,23,9,4]
tgt=19
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==tgt:
            print([i,j])