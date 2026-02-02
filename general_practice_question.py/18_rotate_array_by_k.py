arr=[1,2,3,4,5,6] #o/p=[5,6,1,2,3,4]
n=len(arr)
k=2
k=k%n

for _ in range(k):
    lst=arr.pop()
    arr.insert(0,lst)

print(arr)
