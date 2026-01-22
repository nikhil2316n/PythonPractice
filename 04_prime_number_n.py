x=7
count=0
for i in range(x+1):
    for j in range(1,i+1):
        if i%j==0:
            count+=1

    if count==2:
        print(f"{i} is a prime number")

    else:
        print(f"{i} is a non prime number")
    count=0
