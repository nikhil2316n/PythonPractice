n=str(12345)
print(n)
print("Reversing a number")
rev_num=''
for i in range(1,len(n)+1):
    rev_num+=n[-i]

print(f"Using String Method:{rev_num}")

n2=12345
rev=0
while n2>0:
    digit=n2%10
    rev=rev *10+digit
    n2=n2//10

print(f"Using Mathametical Calculation{rev}")
