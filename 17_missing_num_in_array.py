arr=[2,3,5,6,8,9]
start=arr[0]
end=arr[-1]
new=[]
for i in range(start,end+1):
    new.append(i)
print(f"Number of elements missing are: {len(new)-len(arr)}")

for j in range(min(arr),max(arr)):
    if j not in arr:
        print(j)
