lst=[1,2,3,4,5,6,7,8]
largest=lst[0]

for i in range(len(lst)):
    if lst[i]>largest:
        largest=lst[i]
lst.remove(largest)
largest=lst[0]
for i in range(len(lst)):
    if lst[i]>largest:
        largest=lst[i]
print(largest)