
# Factorial of a numbers from 1 to 10
for i in range(1,10+1):
    fact=1
    for j in range(1,i):
        fact=fact*j
    print(f"Factorial of { i} is :{fact}")
    

