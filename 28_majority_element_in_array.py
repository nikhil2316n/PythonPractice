arr= [2, 2, 1, 2, 3, 2, 21,1,1,1,1,1,1,1,1]

dict1={}

for i in range(len(arr)):
    dict1[arr[i]]=arr.count(arr[i])

for j,k in dict1.items():
    if k==max(dict1.values()):
        print(f"Majority of elements in array is :{j}")
        print(f"The number of times it is repeated is :{k}")