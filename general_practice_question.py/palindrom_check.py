str1="madam"
temp=""
for i in range(1,len(str1)+1):
    temp=temp+str1[-i]

if str1==temp:
    print("palindrome")

else:
    print("Not a palindrome")