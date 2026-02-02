#Using String methos

n=int(input("Enter the Number"))
b=str(n)

sum=0
for i in range(1,len(b)+1):
    sum=sum+i

print(sum)

#Using mathametical logic
n2=123
sum_digits=0

while n2>0:
    digit=n2%10
    sum_digits+=digit
    n2=n2//10
print(sum_digits)