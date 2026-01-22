num=1221
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

if rev==temp:
    print("It is a palindrome")

else:
    print("It is not a palindrome")