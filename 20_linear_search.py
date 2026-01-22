arr=[]
lg=int(input("Enter the number of elements in the array: "))

for i in range(lg):
     ele=int(input(f"Enter the {i+1} element: "))
     arr.insert(i,ele)

srch=int(input("Enter the search element:"))

for index,value in enumerate(arr):
    if srch==value:
        print(f"Element is found at index: {index}")
        break

else:
    print("Element not found")