arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6]
#output=[2,4]
common=[]
for i in arr1:
    for j in arr2:
        if i==j:
            if i not in common:
                common.append(i)

print(common) 