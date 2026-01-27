arr=[1,6,5,3,9,8,7]
arr.sort()
max=arr[0]

for i in arr:
    if i>max:
        max=i

print(max)