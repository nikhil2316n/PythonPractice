n=int(input("Enter the number"))

if n<=1:
    print("Not a Prime Number")
else:
    for i in range(2,n):
        if n%i==0:
            print("Not a Prime Number")
        
    else:
        print("Prime Number")
