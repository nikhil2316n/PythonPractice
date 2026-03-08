arr=[1,2,3,4,6,7,8,9]

max=arr[-1]

actual_sum=sum(arr)

expected_sum=max*(max+1)//2
missed=expected_sum-actual_sum
print("Method 1")
print(f"Missing Number: {missed}")
#Problem here is if there are more than 2 numbers missed in a array then it give the incorrect answer 
#works only when there is only 1 number is missed

new_arr=[]
min=arr[0]
for i in  range(min,max+1):
    new_arr.append(i)

print("Method 2")
for j in range(min,max):
    if j not in arr:
        print(f"Missing number:{j}")

#By this method we can find more than 1 missing elements in the array