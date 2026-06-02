numbers=[2,7,11,15]
tgt=9
left=0
right=len(numbers)-1

while(left<right):
    if(numbers[left]+numbers[right]==tgt):
        print(left,right)
        break
    elif(numbers[left]+numbers[right]>tgt):
        right-=1

    else:
        left+=1

