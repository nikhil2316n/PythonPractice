arr=[11,12,13,14,15,16,17,18]
#11,12,13,14,15,16,17,18
# 0, 1, 2, 3, 4, 5, 6, 7

for k in range(1,len(arr)+1):
    print(f'sub array of length {k}')
    for j in range(len(arr)-k+1):
        
        for i in range(j,j+k):
            print(arr[i],end=' ')
        print(' ')
    
        

    
        